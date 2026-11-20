from product import Product
from orderline import OrderLine
from discount_strategy import DiscountStrategy, NoDiscount

class Order:
    def __init__(self, order_id: str, discount: DiscountStrategy | None = None) -> None:
        self.order_id = order_id
        self.order_lines: list[OrderLine] = []
        self.discount = discount if discount is not None else NoDiscount()

    def get_order_id(self) -> str:
        return self.order_id

    def get_order_lines(self) -> list[OrderLine]:
        return self.order_lines

    def add_order_line(self, product: Product, quantity: int) -> None:
        self.order_lines.append(OrderLine(product, quantity))

    def set_discount(self, discount: DiscountStrategy) -> None:
        if not isinstance(discount, DiscountStrategy):
            raise TypeError("Discount must be a DiscountStrategy.")
        self.discount = discount

    def calculate_total(self) -> float:
        total = sum(line.calculate_subtotal() for line in self.order_lines)
        return self.discount.apply(total)
