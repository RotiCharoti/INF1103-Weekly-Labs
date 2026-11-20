import csv
from inventory import Inventory
from supplier import Supplier
from product_factory import ProductFactory

def load_products(path: str, inventory: Inventory, supplier: Supplier) -> None:
    loaded = 0
    try:
        file = open(path, newline="", encoding="utf-8")
    except FileNotFoundError:
        print(f"Products file not found: {path}")
    else:
        with file:
            reader = csv.reader(file)
            next(reader, None)
            for row_number, row in enumerate(reader, start=2):
                try:
                    if len(row) != 5:
                        raise ValueError("Expected five CSV columns.")
                    kind, product_id, name, price_text, stock_text = row
                    product = ProductFactory.create(
                        kind.strip(), product_id.strip(), name.strip(),
                        float(price_text), int(stock_text), supplier,
                        weight=0.0 if kind.strip() == "physical" else None,
                        download_size=0.0 if kind.strip() == "digital" else None,
                    )
                    inventory.add_product(product)
                    loaded += 1
                except ValueError as error:
                    print(f"Skipping row {row_number}: {error}")
        print(f"{loaded} products loaded.")
    finally:
        print("Load attempt finished.")
