def display_menu():
    print("\n========================================")
    print("       SALES RECORD MANAGEMENT SYSTEM")
    print("========================================")
    print("1. Add Sale Record")
    print("2. View All Records & Summary Statistics")
    print("3. Clear All Sales Data")
    print("4. Exit System")
    print("========================================")

def add_sale_record():
    item_name = input("Enter item name: ")

    if not item_name:
        print("Item name cannot be empty.")
        return

    try:
        quantity = int(input("Enter quantity sold: "))

        if quantity < 0:
            print("Quantity cannot be negative.")
            return
    except ValueError:
        print("Invalid quantity. Please enter a digit")
        return

    try:
        price_per_unit = float(input("Enter price per unit: "))

        if price_per_unit < 0:
            print("Price cannot be negative.")
            return
    except ValueError:
        print("Invalid price. Please enter a number.")
        return

    total_amount = quantity * price_per_unit

    try:
        with open(sales_log.txt, "a") as file:
            file.write(
                f"{item_name},{quantity},{price_per_unit},"
                f"{total_amount:}\n"
            )

    except OSError:
        print("Error saving the sale record")


if choice == "1":
    itemName = input("Enter Item Name:")
    quantitySold = int(input("Enter Item Quantity Sold: "))
    perUnit = float(input("Enter Item Price /unit: "))
    total = quantitySold * perUnit
    print(itemName, quantitySold, perUnit, total)

elif choice == "2":
    exit()

elif choice == "4":
    print("Thank you for using the Sales Record Management System.")
    exit()

