
from abc import ABC, abstractmethod
from supplier import Supplier


class Product(ABC):
    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock_quantity: int,
        supplier: Supplier
    ) -> None:

        if not product_id.strip():
            raise ValueError("Product ID cannot be empty.")

        if not name.strip():
            raise ValueError("Product name cannot be empty.")

        if price <= 0:
            raise ValueError("Product price must be greater than zero.")

        if stock_quantity < 0:
            raise ValueError("Stock quantity cannot be less than 0.")

        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock_quantity = stock_quantity
        self.__supplier = supplier

    def get_product_id(self) -> str:
        return self.__product_id

    def get_name(self) -> str:
        return self.__name

    def get_price(self) -> float:
        return self.__price

    def get_stock(self) -> int:
        return self.__stock_quantity

    def get_supplier(self) -> Supplier:
        return self.__supplier

    def update_stock(self, quantity: int) -> None:
        if quantity < 0:
            raise ValueError("Stock quantity cannot be less than 0.")

        self.__stock_quantity = quantity

    def display_information(self) -> str:
        return (
            f"Product ID: {self.__product_id} | "
            f"Product Name: {self.__name} | "
            f"Price: ${self.__price:.2f} | "
            f"Stock: {self.__stock_quantity} units | "
            f"Supplier ID: {self.__supplier.get_supplier_id()} | "
            f"Supplier Name: {self.__supplier.get_supplier_name()} | "
            f"Supplier Contact: {self.__supplier.get_supplier_contact_email()}"
        )

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass
