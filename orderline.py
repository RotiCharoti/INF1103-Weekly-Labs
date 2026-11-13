from product import Product

class OrderLine:
    def __init__(self, product: Product, quantity: int) -> None:
        self.product = product
        self.quantity = quantity

    def get_product(self) -> Product:
        return self.product
    
    def get_quantity(self) -> int:
        return self.quantity
    
    def calculate_subtotal(self) -> float:
        return self.product.get_price() * self.quantity