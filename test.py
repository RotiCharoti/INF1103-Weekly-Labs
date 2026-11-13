
from digital_product import DigitalProduct
from inventory import Inventory
from order import Order
from physical_product import PhysicalProduct
from product import Product
from supplier import Supplier


def test_association() -> None:
    print("===== Association Test =====")

    apple = Supplier("S002", "Apple", "apple@gmail.com")
    iphone = PhysicalProduct(
        "P001", "iPhone", 999.00, 20, apple, 0.5
    )

    del apple

    print("\n===== Product Information =====")
    print(iphone.display_information())


def test_aggregation() -> None:
    print("===== Aggregation Test =====")

    nvidia = Supplier("S001", "Nvidia", "nvidia@gmail.com")

    microchip = PhysicalProduct(
        "P002", "Microchip", 1200.00, 15, nvidia, 2.5
    )

    inventory_A = Inventory()

    inventory_A.add_product(microchip)
    inventory_A.remove_product("P002")

    print("\n===== Microchip Information =====")
    print(microchip.display_information())

    print("\n===== Inventory A =====")
    inventory_A.display_all()

    inventory_B = Inventory()
    inventory_B.add_product(microchip)

    print("\n===== Inventory B =====")
    inventory_B.display_all()


def test_composition() -> None:
    print("===== Composition Test =====")

    apple = Supplier("S002", "Apple", "apple@gmail.com")

    silicon_chip = PhysicalProduct(
        "P002", "Microchip", 1200.00, 15, apple, 2.5
    )

    order1 = Order("1")
    order1.add_order_line(silicon_chip, 10)

    orderline1 = order1.get_order_lines()[0]

    order2 = Order("2")
    order2.add_order_line(silicon_chip, 5)

    orderline2 = order2.get_order_lines()[0]

    print(
        f"OrderLine 1 and OrderLine 2 are the same: "
        f"{orderline1 is orderline2}"
    )

    print(
        f"Product object for order1 and order2 are the same: "
        f"{orderline1.get_product() is orderline2.get_product()}"
    )

    print(f"\nOrder 1 Total: ${order1.calculate_total():.2f}")
    print(f"Order 2 Total: ${order2.calculate_total():.2f}")


def show_product_details(product: Product) -> None:
    print(product.display_information())
    print(product.get_fulfilment_info())


def test_substitutability() -> None:
    print("===== Substitutability Test =====")

    mojang = Supplier("S003", "Mojang", "mojang@gmail.com")
    samsung = Supplier("S004", "Samsung", "samsung@gmail.com")

    minecraft = DigitalProduct(
        "D001", "Minecraft", 15.0, 999, mojang, 5.2
    )

    earbuds = PhysicalProduct(
        "P001", "Earbuds", 25.0, 100, samsung, 0.1
    )

    print("\n===== Digital Product Details =====")
    show_product_details(minecraft)

    print("\n===== Physical Product Details =====")
    show_product_details(earbuds)


def test_polymorphism() -> None:
    print("===== Polymorphism Test =====")

    mojang = Supplier("S003", "Mojang", "mojang@gmail.com")
    samsung = Supplier("S004", "Samsung", "samsung@gmail.com")

    minecraft = DigitalProduct(
        "D001", "Minecraft", 15.0, 999, mojang, 5.2
    )

    earbuds = PhysicalProduct(
        "P001", "Earbuds", 25.0, 100, samsung, 0.1
    )

    inventory = Inventory()

    inventory.add_product(minecraft)
    inventory.add_product(earbuds)

    for product in inventory.get_products():
        print(product.display_information())
        print(product.get_fulfilment_info())
        print()

    print("===== Using show_product_details Function =====")

    show_product_details(minecraft)
    show_product_details(earbuds)


test_association()
test_aggregation()
test_composition()
test_substitutability()
test_polymorphism()
