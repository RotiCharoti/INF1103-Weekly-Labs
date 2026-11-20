from product import Product
from can_be_shipped import CanBeShipped
from supplier import Supplier

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier, weight: float) -> None:
        if weight < 0:
            raise ValueError("Product weight cannot be less than 0.")

        super().__init__(product_id, name, price, stock, supplier)
        self._weight = weight

    def get_weight(self) -> float:
        return self._weight

    def display_information(self) -> str:
        return (
            f"{super().display_information()} | "
            f"Weight: {self._weight:.2f} kg"
        )

    def get_fulfilment_info(self) -> str:
        return "This product requires physical shipping."

    def calculate_shipping_cost(self) -> float:
        return self._weight * 2.00
