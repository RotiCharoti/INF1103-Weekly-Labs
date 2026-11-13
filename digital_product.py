from product import Product
from supplier import Supplier

class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier, download_size: float) -> None:
        if download_size < 0:
            raise ValueError("Download size cannot be less than 0.")

        super().__init__(product_id, name, price, stock, supplier)
        self._download_size = download_size

    def get_download_size(self) -> float:
        return self._download_size

    def display_information(self) -> str:
        return (
            f"{super().display_information()} | "
            f"Download Size: {self._download_size:.2f} MB"
        )

    def get_fulfilment_info(self) -> str:
        return "This product will be delivered digitally."
