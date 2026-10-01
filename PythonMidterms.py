FILE_NAME = "sales_log.txt"
def display_menu():
    print("========================================")
    print("       SALES RECORD MANAGEMENT SYSTEM")
    print("========================================")
    print("1. Add Sale Record")
    print("2. View All Records & Summary Statistics")
    print("3. Clear All Sales Data")
    print("4. Exit System")
    print("========================================")

def main():
    while True:
        display_menu()
        choice = input("Select an option (1-4): ")

        if choice == "1":
            add_sale_record()

        elif choice == "2":
            print("placeholder")

        elif choice == "3":
            clear_sales_data()

        elif choice == "4":
            print("Thank you for using the Sales Record Management System.")
            break

        else:
            print("Invalid option. Please select a number from 1 to 4.")

def add_sale_record():
    item_name = input("Enter item name: ")

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
        with open(FILE_NAME, "a") as file:
            file.write(
                f"{item_name},{quantity},{price_per_unit:.},"
                f"{total_amount}"
            )

        print("Sale record saved successfully.")

    except:
        print("Error saving the sale record:")

def clear_sales_data():
    try:
        with open(FILE_NAME, "w"):
            pass

        print("All records cleared. No records remaining.")

    except:
        print("Error clearing sales data:")

if __name__ == "__main__":
    main()

def view_records():
    print("\n--- All Sales Records ---")

    total_units = 0
    grand_total_revenue = 0.0
    records_found = False

    try:
        with open(FILE_NAME, "r",) as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                record = line.split(",")

                if len(record) != 4:
                    print("Warning: Invalid record skipped.")
                    continue

                try:
                    item_name = record[0]
                    quantity = int(record[1])
                    price_per_unit = float(record[2])
                    total_amount = float(record[3])

                    print(f"\nItem Name: {item_name}")
                    print(f"Quantity Sold: {quantity}")
                    print(f"Price Per Unit: {price_per_unit:.2f}")
                    print(f"Total Amount: {total_amount:.2f}")

                    total_units += quantity
                    grand_total_revenue += total_amount
                    records_found = True

                except ValueError:
                    print("Warning: Invalid data in record. Skipped.")

    except FileNotFoundError:
        print("No records found.")
        return

    except:
        print("Error reading the sales file:")
        return

    if not records_found:
        print("No records found.")
        return

    print("\n========================================")
    print("          SUMMARY STATISTICS")
    print("========================================")
    print(f"Total Units Sold: {total_units}")
    print(f"Grand Total Revenue: {grand_total_revenue:.2f}")
def view_records():
    print("\n--- All Sales Records ---")

    total_units = 0
    grand_total_revenue = 0.0
    records_found = False


    try:
        with open(FILE_NAME, "r",) as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                record = line.split(",")

                if len(record) != 4:
                    print("Warning: Invalid record skipped.")
                    continue

                try:
                    item_name = record[0]
                    quantity = int(record[1])
                    price_per_unit = float(record[2])
                    total_amount = float(record[3])

                    # Display the current record.
                    print(f"\nItem Name: {item_name}")
                    print(f"Quantity Sold: {quantity}")
                    print(f"Price Per Unit: {price_per_unit:.2f}")
                    print(f"Total Amount: {total_amount:.2f}")


                    total_units += quantity
                    grand_total_revenue += total_amount
                    records_found = True

                except ValueError:
                    print("Warning: Invalid data in record. Skipped.")

    except FileNotFoundError:
        print("No records found.")
        return

    except :
        print("Error reading the sales file")
        return

    if not records_found:
        print("No records found.")
        return

    print("========================================")
    print("          SUMMARY STATISTICS")
    print("========================================")
    print(f"Total Units Sold: {total_units}")
    print(f"Grand Total Revenue: {grand_total_revenue}")
