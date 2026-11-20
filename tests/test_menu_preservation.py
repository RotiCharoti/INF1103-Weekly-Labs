import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch
from app import add_product_option, display_menu
from inventory import Inventory
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

class MenuPreservationTests(unittest.TestCase):
    def test_original_menu(self):
        output=io.StringIO()
        with redirect_stdout(output): display_menu()
        self.assertNotIn("Load Products from CSV", output.getvalue())
        self.assertIn("6. Exit", output.getvalue())
        for label in ("Display All Products", "Add Product", "Update Stock", "Search Product", "Save Inventory", "Exit"):
            self.assertIn(label,output.getvalue())
    def test_physical_selection(self):
        inv=Inventory()
        answers=["1","PNEW","Lamp","25","3","S1","Supplier","s@example.com","2"]
        with patch("builtins.input",side_effect=answers),redirect_stdout(io.StringIO()): add_product_option(inv)
        self.assertIsInstance(inv.get_products()[0],PhysicalProduct)
    def test_digital_selection(self):
        inv=Inventory()
        answers=["2","DNEW","Software","50","4","S1","Supplier","s@example.com","100"]
        with patch("builtins.input",side_effect=answers),redirect_stdout(io.StringIO()): add_product_option(inv)
        self.assertIsInstance(inv.get_products()[0],DigitalProduct)
if __name__=="__main__": unittest.main()
