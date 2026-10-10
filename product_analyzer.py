
import json


DATA_FILE = "products.json"


def load_products():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Error: products.json contains invalid JSON.")
        return []


products = load_products()


def save_products():
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(products, file, indent=4, ensure_ascii=False)


def find_products_by_name(product_name):
    return [
        product for product in products
        if product_name.strip().lower() in product["name"].lower()
    ]


def product_name_exists(name, exclude_id=None):
    for product in products:
        if product["name"].strip().lower() == name.strip().lower():
            if product["id"] != exclude_id:
                return True
    return False


def find_product(product_id):
    for product in products:
        if product["id"] == product_id:
            return product
    return None


def get_product_id():
    try:
        return int(input("Enter product ID: "))
    except ValueError:
        print("Please enter a valid number!")
        return None


def generate_product_id():
    return max((product["id"] for product in products), default=0) + 1


def calculate_decision(profit_margin):
    if profit_margin >= 40:
        return "scale"
    elif profit_margin >= 30:
        return "keep"
    return "review"



def analyze_product(product):
    quantity = product["quantity"]
    purchase_price = product["purchase_price"]
    selling_price = product["selling_price"]
    shipping = product["shipping"]

    product_cost = purchase_price * quantity
    revenue = selling_price * quantity
    total_cost = product_cost + shipping
    profit = revenue - total_cost

    profit_margin = profit / revenue * 100 if revenue > 0 else 0

    decision = calculate_decision(profit_margin)

    if profit_margin >= 30:
        status = "good"
    elif profit_margin >= 15:
        status = "medium"
    else:
        status = "bad"

    return {
        "id": product["id"],
        "name": product["name"],
        "cost": product_cost,
        "revenue": revenue,
        "total_cost": total_cost,
        "profit": profit,
        "profit_margin": profit_margin,
        "status": status,
        "decision": decision
    }



def calculate_total_profit(results):
    return sum(result["profit"] for result in results)


def calculate_best_profit_and_product(results):
    if not results:
        return None, None

    best = max(results, key=lambda result: result["profit"])
    return best["profit"], best["name"]


def calculate_worst_profit_and_product(results):
    if not results:
        return None, None

    worst = min(results, key=lambda result: result["profit"])
    return worst["name"], worst["profit"]


def final_report(results):
    if not results:
        print("No products available for the report.")
        return

    print("\n===== BUSINESS REPORT =====")
    print("Total Profit:", calculate_total_profit(results))

    best_profit, best_product = calculate_best_profit_and_product(results)
    print("Best Product:", best_product)
    print("Best Profit:", best_profit)

    worst_product, worst_profit = calculate_worst_profit_and_product(results)
    print("Worst Product:", worst_product)
    print("Worst Profit:", worst_profit)

    print("\nProduct Decisions:")
    for result in results:
        print(
            f'{result["name"]} → {result["decision"]} '
            f'(Margin: {result["profit_margin"]:.1f}%)'
        )


def create_product():
    while True:
        name = input("Product name: ").strip()

        if not name:
            print("Product name cannot be empty!")
        elif product_name_exists(name):
            print("Product already exists!")
        else:
            break

    values = {}

    for field, prompt, allow_zero in [
        ("purchase_price", "Purchase price: ", False),
        ("quantity", "Quantity: ", False),
        ("shipping", "Shipping: ", True),
        ("selling_price", "Selling price: ", False),
    ]:
        while True:
            try:
                value = int(input(prompt))

                if value < 0 or (value == 0 and not allow_zero):
                    print("Invalid value. Please try again.")
                    continue

                values[field] = value
                break
            except ValueError:
                print("Please enter a whole number!")

    return {
        "id": generate_product_id(),
        "name": name,
        **values
    }


def update_product():
    product_id = get_product_id()
    if product_id is None:
        return

    product = find_product(product_id)
    if product is None:
        print("Product not found!")
        return

    fields = {
        "2": ("purchase_price", "New purchase price: ", False),
        "3": ("quantity", "New quantity: ", False),
        "4": ("shipping", "New shipping cost: ", True),
        "5": ("selling_price", "New selling price: ", False),
    }

    while True:
        print("\n===== UPDATE PRODUCT =====")
        print("1. Product Name")
        print("2. Purchase Price")
        print("3. Quantity")
        print("4. Shipping")
        print("5. Selling Price")
        print("6. Back to Menu")

        choice = input("Choose an option: ")

        if choice == "1":
            new_name = input("New product name: ").strip()

            if not new_name:
                print("Product name cannot be empty!")
            elif product_name_exists(new_name, product["id"]):
                print("Product name already exists!")
            else:
                product["name"] = new_name
                save_products()
                print("Product name updated successfully!")

        elif choice in fields:
            field, prompt, allow_zero = fields[choice]

            while True:
                try:
                    value = int(input(prompt))

                    if value < 0 or (value == 0 and not allow_zero):
                        print("Invalid value. Please try again.")
                        continue

                    product[field] = value
                    save_products()
                    print("Product updated successfully!")
                    break
                except ValueError:
                    print("Please enter a whole number!")

        elif choice == "6":
            break
        else:
            print("Invalid choice!")


def main():
    while True:
        print("\n===== PRODUCT MANAGER =====")
        print("1. Search Product")
        print("2. Add Product")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Show Report")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter product name: ")
            results = find_products_by_name(name)

            if results:
                for product in results:
                    print(
                        "ID:", product["id"],
                        "| Name:", product["name"],
                        "| Selling Price:", product["selling_price"]
                    )
            else:
                print("Product not found!")

        elif choice == "2":
            new_product = create_product()
            products.append(new_product)
            save_products()
            print("Product added successfully!")

        elif choice == "3":
            update_product()

        elif choice == "4":
            product_id = get_product_id()

            if product_id is None:
                continue

            product = find_product(product_id)

            if product is None:
                print("Product not found!")
            else:
                confirm = input(
                    f'Delete "{product["name"]}"? (y/n): '
                ).strip().lower()

                if confirm == "y":
                    products.remove(product)
                    save_products()
                    print("Product deleted successfully!")
                else:
                    print("Deletion cancelled.")

        elif choice == "5":
            results = [analyze_product(product) for product in products]
            final_report(results)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
