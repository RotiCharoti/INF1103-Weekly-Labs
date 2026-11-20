from product import Product

class Inventory:
    def __init__(self) -> None:
        self.products: list[Product] = []

    def get_products(self) -> list[Product]:
        return list(self.products)
    
    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def search_product(self, product_id: str) -> Product | None:
        for product in self.products:
            if product.get_product_id() == product_id:
                return product
        return None
    
    def remove_product(self, product_id: str) -> bool:
        product = self.search_product(product_id)
        if product:
            self.products.remove(product)
            return True
        return False
    
    def display_all_products(self) -> None:
        print("Current Inventory")
        print("------------------------------------------------")

        if not self.products:
            print("Inventory is empty.")
            return

        for product in self.products:
            print(product.display_information())

    def display_all(self) -> None:
        self.display_all_products()
