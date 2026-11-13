from product import Product
from orderline import OrderLine

class Order:
    def __init__(self, order_id: str) -> None:
        self.order_id = order_id
        self.order_lines: list[OrderLine] = []

    def get_order_id(self) -> str:
        return self.order_id

    def get_order_lines(self) -> list[OrderLine]:
        return self.order_lines

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.order_lines.append(order_line)

    def calculate_total(self) -> float:
        return sum(line.calculate_subtotal() for line in self.order_lines)

