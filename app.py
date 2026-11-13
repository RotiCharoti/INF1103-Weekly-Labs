
import json

from digital_product import DigitalProduct
from inventory import Inventory
from physical_product import PhysicalProduct
from supplier import Supplier
from can_be_shipped import CanBeShipped


FILENAME = "inventory.json"


def product_to_dictionary(product: PhysicalProduct | DigitalProduct) -> dict:
    supplier = product.get_supplier()

    common_data = {
        "id": product.get_product_id(),
        "name": product.get_name(),
        "price": product.get_price(),
        "stock": product.get_stock(),
        "supplier": {
            "supplier_id": supplier.get_supplier_id(),
            "name": supplier.get_supplier_name(),
            "contact_email": supplier.get_supplier_contact_email()
        }
    }

    if isinstance(product, PhysicalProduct):
        common_data["type"] = "physical"
        common_data["weight"] = product.get_weight()

    elif isinstance(product, DigitalProduct):
        common_data["type"] = "digital"
        common_data["download_size"] = product.get_download_size()

    return common_data


def save_inventory(inventory: Inventory) -> None:
    data = [
        product_to_dictionary(product)
        for product in inventory.get_products()
    ]

    with open(FILENAME, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_inventory() -> Inventory:
    inventory = Inventory()

    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            data = json.load(file)

        for item in data:
            supplier_data = item.get("supplier")

            # Support older inventory.json files without supplier information
            if supplier_data is None:
                supplier = Supplier(
                    "S000",
                    "Unknown Supplier",
                    "unknown@example.com"
                )
            else:
                supplier = Supplier(
                    supplier_data["supplier_id"],
                    supplier_data["name"],
                    supplier_data["contact_email"]
                )

            product_type = item.get("type")

            if product_type == "physical":
                product = PhysicalProduct(
                    item["id"],
                    item["name"],
                    item["price"],
                    item["stock"],
                    supplier,
                    item["weight"]
                )

            elif product_type == "digital":
                product = DigitalProduct(
                    item["id"],
                    item["name"],
                    item["price"],
                    item["stock"],
                    supplier,
                    item["download_size"]
                )

            else:
                print(
                    f"Skipping product {item.get('id', 'unknown')}: "
                    "missing or invalid product type."
                )
                continue

            inventory.add_product(product)

    except FileNotFoundError:
        # Create sample data if inventory file does not exist

        supplier1 = Supplier(
            "S001", "Tech Supplies", "tech@gmail.com"
        )

        supplier2 = Supplier(
            "S002", "Software Solutions", "software@gmail.com"
        )

        inventory.add_product(
            PhysicalProduct(
                "P001", "Laptop", 1200.00, 15, supplier1, 2.5
            )
        )

        inventory.add_product(
            PhysicalProduct(
                "P002", "Mouse", 25.50, 40, supplier1, 0.2
            )
        )

        inventory.add_product(
            DigitalProduct(
                "D001", "Antivirus Software", 39.90, 100,
                supplier2, 250
            )
        )

        save_inventory(inventory)

    except (json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
        print(f"Unable to load inventory data: {error}")
        print("Starting with an empty inventory.")

    return inventory


def display_menu() -> None:
    print("\n----------- MENU ----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("---------------------------")


def create_supplier() -> Supplier:
    print("\nSupplier Information")

    supplier_id = input("Supplier ID: ").strip()
    supplier_name = input("Supplier Name: ").strip()
    supplier_email = input("Supplier Contact Email: ").strip()

    return Supplier(
        supplier_id,
        supplier_name,
        supplier_email
    )


def add_product_option(inventory: Inventory) -> None:
    print("\nSelect Product Type")
    print("1. Physical Product")
    print("2. Digital Product")

    choice = input("Enter option: ").strip()

    if choice not in ("1", "2"):
        print("Invalid product type. Please enter 1 or 2.")
        return

    try:
        product_id = input("Product ID: ").strip()
        name = input("Product Name: ").strip()
        price = float(input("Price: ").strip())
        stock = int(input("Stock Quantity: ").strip())

        supplier = create_supplier()

        if choice == "1":
            weight = float(input("Weight (kg): ").strip())

            product = PhysicalProduct(
                product_id,
                name,
                price,
                stock,
                supplier,
                weight
            )

        else:
            download_size = float(
                input("Download Size (MB): ").strip()
            )

            product = DigitalProduct(
                product_id,
                name,
                price,
                stock,
                supplier,
                download_size
            )

    except ValueError as error:
        print(f"Invalid input! {error}")
        return

    inventory.add_product(product)
    print("Product added successfully!")


def update_stock_option(inventory: Inventory) -> None:
    print("\nUpdate Stock")

    product_id = input("Enter Product ID: ").strip()
    product = inventory.search_product(product_id)

    if product is None:
        print("No product found.")
        return

    print(f"Name: {product.get_name()}")
    print(f"Current Stock: {product.get_stock()}")

    try:
        new_stock = int(input("New Stock Quantity: ").strip())
        product.update_stock(new_stock)

        print("Stock updated successfully!")

    except ValueError as error:
        print(f"Invalid input! {error}")


def search_product_option(inventory: Inventory) -> None:
    print("\nSearch Product")

    product_id = input("Enter Product ID: ").strip()
    product = inventory.search_product(product_id)

    if product is None:
        print("No product found.")

    else:
        print(product.display_information())
        print(product.get_fulfilment_info())

        if isinstance(product, CanBeShipped):
            print(
                f"Shipping Cost: "
                f"${product.calculate_shipping_cost():.2f}"
            )


def main() -> None:
    inventory = load_inventory()

    while True:
        display_menu()
        choice = input("\nEnter option: ").strip()

        if choice == "1":
            inventory.display_all()

        elif choice == "2":
            add_product_option(inventory)

        elif choice == "3":
            update_stock_option(inventory)

        elif choice == "4":
            search_product_option(inventory)

        elif choice == "5":
            save_inventory(inventory)
            print(f"Inventory saved successfully to {FILENAME}.")

        elif choice == "6":
            save_inventory(inventory)
            print("Inventory saved successfully.")
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break

        else:
            print("Invalid option! Please enter a valid option (1-6).")


if __name__ == "__main__":
    main()
