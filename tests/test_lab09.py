import io
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch
from supplier import Supplier
from product_factory import ProductFactory
from inventory import Inventory
from order import Order
from discount_strategy import NoDiscount, PercentageDiscount, BulkDiscount, StudentDiscount, DiscountStrategy
from input_helpers import get_positive_float
from csv_loader import load_products

class Lab09Tests(unittest.TestCase):
    def setUp(self):
        self.supplier = Supplier("S1", "Test", "test@example.com")
        self.product = ProductFactory.create("physical", "P1", "Example", 25, 10, self.supplier, weight=1)

    def test_strategy_and_switch(self):
        order = Order("O1", BulkDiscount(200, 20))
        order.add_order_line(self.product, 10)
        self.assertEqual(order.calculate_total(), 230)
        order.set_discount(PercentageDiscount(10))
        self.assertEqual(order.calculate_total(), 225)
        order.set_discount(StudentDiscount())
        self.assertEqual(order.calculate_total(), 237.5)
        order.set_discount(NoDiscount())
        self.assertEqual(order.calculate_total(), 250)

    def test_new_strategy_without_changing_order(self):
        class FlatFive(DiscountStrategy):
            def apply(self, total): return total - 5
        order = Order("O2", FlatFive())
        order.add_order_line(self.product, 1)
        self.assertEqual(order.calculate_total(), 20)

    def test_factory_types_and_unknown(self):
        self.assertEqual(self.product.get_weight(), 1)
        digital = ProductFactory.create("digital", "D1", "File", 5, 1, self.supplier, download_size=12)
        self.assertEqual(digital.get_download_size(), 12)
        with self.assertRaisesRegex(ValueError, "Unknown product type: service"):
            ProductFactory.create("service", "S1", "Service", 5, 1, self.supplier)

    def test_validation(self):
        with self.assertRaises(ValueError): ProductFactory.create("physical", "P2", "Bad", 0, 1, self.supplier, weight=1)
        with self.assertRaises(ValueError): ProductFactory.create("digital", "D2", "Bad", 1, -1, self.supplier, download_size=1)
        with self.assertRaises(ValueError): Order("O3").add_order_line(self.product, 0)
        with self.assertRaises(ValueError): self.product.update_stock(-1)

    def test_input_retry(self):
        output = io.StringIO()
        with patch("builtins.input", side_effect=["abc", "-5", "12.50"]), redirect_stdout(output):
            self.assertEqual(get_positive_float("Price: "), 12.5)
        self.assertEqual(output.getvalue().splitlines(), [
            "Please enter a valid number, e.g. 12.50",
            "Please enter a number greater than zero."])

    def test_csv_missing_and_invalid_rows(self):
        inventory = Inventory()
        output = io.StringIO()
        with redirect_stdout(output): load_products("missing_file_123456.csv", inventory, self.supplier)
        self.assertIn("Load attempt finished.", output.getvalue())
        self.assertEqual(len(inventory.get_products()), 0)
        sample = Path(__file__).resolve().parents[1] / "products.csv"
        output = io.StringIO()
        with redirect_stdout(output): load_products(str(sample), inventory, self.supplier)
        self.assertEqual(len(inventory.get_products()), 3)
        self.assertIn("3 products loaded.", output.getvalue())
        self.assertIn("Skipping row 4:", output.getvalue())
        self.assertIn("Skipping row 5:", output.getvalue())

if __name__ == "__main__":
    unittest.main()
