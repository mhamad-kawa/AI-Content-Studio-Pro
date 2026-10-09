import json

product = {
    "id": 1,
    "name": "smart_watch",
    "purchase_price": 20,
    "quantity": 50,
    "shipping": 100,
    "selling_price": 40
}

product2 = {
    "id": 2,
    "name": "Bluetooth Speaker",
    "purchase_price": 15,
    "quantity": 30,
    "shipping": 80,
    "selling_price": 30
}

product3 = {
    "id": 3,
    "name": "USB-C Cable",
    "purchase_price": 3,
    "quantity": 100,
    "shipping": 50,
    "selling_price": 7
}

with open("products.json", "r") as file:
    products = json.load(file)


def find_product_by_name(product_name):
    for product in products:
        if product_name.lower() in product["name"].lower():
            return product

    return None

def find_product(product_id):
    for product in products:
        if product["id"] == product_id:
            return product
    return None


def save_products():
    with open("products.json", "w") as file:
        json.dump(products, file, indent=4)


def get_product_id():
    try:
        product_id = int(input("Enter product ID: "))
        return product_id
    except ValueError:
        print("Please enter a number!")
        return None


def calculate_decision(profit_margin):
    if profit_margin >= 40:
        return "scale"
    elif profit_margin >= 30:
        return "keep"
    else:
        return "review"


def analyze_product(product):

    product_cost = product["purchase_price"] * product["quantity"]

    revenue = product["selling_price"] * product["quantity"]

    total_cost = product_cost + product["shipping"]

    profit = revenue - total_cost

    profit_margin = profit / revenue * 100

    decision = calculate_decision(profit_margin)

    if profit_margin >= 30:
        status = "good"
    elif profit_margin >= 15:
        status = "medium"
    else:
        status = "bad"

    return {
        "name": product["name"],
        "cost": product_cost,
        "revenue": revenue,
        "total_cost": total_cost,
        "profit": profit,
        "profit_margin": profit_margin,
        "status": status,
        "decision": decision
    }


def calculat_total_profit(results):
    total_profit = 0

    for result in results:
        total_profit = total_profit + result["profit"]

    return total_profit


def calculate_best_profit_and_product(results):
    best_profit = 0
    best_product = ""

    for result in results:
        if result["profit"] > best_profit:
            best_profit = result["profit"]
            best_product = result["name"]

    return best_profit, best_product


def calculate_worst_profit_and_product(results):
    worst_profit = 10000
    worst_product = ""

    for result in results:
        if result["profit"] < worst_profit:
            worst_profit = result["profit"]
            worst_product = result["name"]

    return worst_product, worst_profit

def generate_product_id():
    max_id = 0

    for product in products:
        if product["id"] > max_id:
            max_id = product["id"]

    return max_id + 1

def create_product():

    while True:

        name = input("Product name: ")

        if name.strip() == "":
            print("Product name cannot be empty!")
            continue

        existing_product = find_product_by_name(name)

        if existing_product != None:
            print("Product already exists!")
            continue

        break
   

    # Purchase Price Validation
    while True:
        try:
            purchase_price = int(input("Purchase price: "))

            if purchase_price <= 0:
                print("Invalid purchase price!")
                continue

            break

        except ValueError:
            print("Please enter a number!")

    # Quantity Validation
    while True:
        try:
            quantity = int(input("Quantity: "))

            if quantity <= 0:
                print("Invalid quantity!")
                continue

            break

        except ValueError:
            print("Please enter a number!")

    # Shipping Validation
    while True:
        try:
            shipping = int(input("Shipping: "))

            if shipping < 0:
                print("Invalid shipping!")
                continue

            break

        except ValueError:
            print("Please enter a number!")

    # Selling Price Validation
    while True:
        try:
            selling_price = int(input("Selling price: "))

            if selling_price <= 0:
                print("Invalid selling price!")
                continue

            break

        except ValueError:
            print("Please enter a number!")

    product = {
        "id": generate_product_id(),
        "name": name,
        "purchase_price": purchase_price,
        "quantity": quantity,
        "shipping": shipping,
        "selling_price": selling_price
    }
    


    return product


def final_report(results):

    total_profit = calculat_total_profit(results)

    print("Total Profit:", total_profit)

    best_profit, best_product = calculate_best_profit_and_product(results)

    print("Best Product:", best_product)

    print("Best Profit:", best_profit)

    worst_product, worst_profit = calculate_worst_profit_and_product(results)

    print("Worst Product:", worst_product)

    print("Worst Profit:", worst_profit)

    print("\nProduct Decisions:")

    for result in results:
        print(result["name"], "→", result["decision"])


# ==============================
# PRODUCT MANAGER
# ==============================

while True:

    print("\n===== PRODUCT MANAGER =====")
    print("1. Search Product")
    print("2. Add Product")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Show Report")
    print("6. Exit")

    choice = input("Choose an option: ")

    # SEARCH
    if choice == "1":

        product_name = input("Enter product name: ")

        result = find_product_by_name(product_name)

        if result != None:
            print("Product found:", result["name"])
        else:
            print("Product not found!")

    # ADD
    elif choice == "2":

        new_product = create_product()

        products.append(new_product)

        save_products()

        print("Product added successfully!")

        # UPDATE
    elif choice == "3":

        product_id = get_product_id()

        if product_id is None:
            continue

        result = find_product(product_id)

        if result is None:
            print("Product not found!")
            continue

        while True:
            print("\nWhat do you want to update?")
            print("1. Product Name")
            print("2. Purchase Price")
            print("3. Quantity")
            print("4. Shipping")
            print("5. Selling Price")
            print("6. Back to Menu")

            update_choice = input("Choose an option: ")

            if update_choice == "1":

                while True:
                    new_name = input("Enter new product name: ").strip()

                    if new_name == "":
                        print("Product name cannot be empty!")
                        continue

                    existing_product = find_product_by_name(new_name)

                    if existing_product is not None and existing_product["id"] != result["id"]:
                        print("Product name already exists!")
                        continue

                    break

                result["name"] = new_name
                save_products()

                print("Product name updated successfully:", result["name"])

            elif update_choice == "2":

                while True:
                    try:
                        new_purchase_price = int(
                            input("Enter new purchase price: ")
                        )

                        if new_purchase_price <= 0:
                            print("Purchase price must be greater than zero!")
                            continue

                        break

                    except ValueError:
                        print("Please enter a number!")

                result["purchase_price"] = new_purchase_price
                save_products()

                print(
                    "Purchase price updated successfully:",
                    result["purchase_price"]
                )

            elif update_choice == "3":

                while True:
                    try:
                        new_quantity = int(input("Enter new quantity: "))

                        if new_quantity <= 0:
                            print("Quantity must be greater than zero!")
                            continue

                        break

                    except ValueError:
                        print("Please enter a number!")

                result["quantity"] = new_quantity
                save_products()

                print("Quantity updated successfully:", result["quantity"])
            elif update_choice == "4":

                while True:
                    try:
                        new_shipping = int(input("Enter new shipping cost: "))

                        if new_shipping < 0:
                            print("Shipping cannot be negative!")
                            continue

                        break

                    except ValueError:
                        print("Please enter a number!")

                result["shipping"] = new_shipping
                save_products()

                print("Shipping updated successfully:", result["shipping"])

            elif update_choice == "5":

                while True:
                    try:
                        new_selling_price = int(
                            input("Enter new selling price: ")
                        )

                        if new_selling_price <= 0:
                            print("Selling price must be greater than zero!")
                            continue

                        break

                    except ValueError:
                        print("Please enter a number!")

                result["selling_price"] = new_selling_price
                save_products()

                print(
                    "Selling price updated successfully:",
                    result["selling_price"]
                )

            elif update_choice == "6":
                print("Back to Menu")
                break

    # DELETE
    elif choice == "4":

        product_id = get_product_id()

        if product_id == None:
            continue

        result = find_product(product_id)

        if result != None:

            products.remove(result)

            save_products()

            print("Product deleted successfully!")

        else:
            print("Product not found!")

    # REPORT
    elif choice == "5":

        results = []

        for product in products:
            result = analyze_product(product)
            results.append(result)

        final_report(results)

    # EXIT
    elif choice == "6":

        print("Goodbye!")

        break

    else:
        print("Invalid choice!")