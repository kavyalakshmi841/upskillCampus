import os

FILE = "expenses.txt"

def add_expense():
    date = input("Date (DD-MM-YYYY): ")
    category = input("Category: ")
    amount = input("Amount: ")
    description = input("Description: ")

    with open(FILE, "a") as f:
        f.write(f"{date},{category},{amount},{description}\n")

    print("Expense Added Successfully.")

def view_expenses():
    if not os.path.exists(FILE):
        print("No expenses found.")
        return

    print("\n------ Expenses ------")
    with open(FILE, "r") as f:
        for line in f:
            data = line.strip().split(",")
            print(f"Date: {data[0]}")
            print(f"Category: {data[1]}")
            print(f"Amount: ₹{data[2]}")
            print(f"Description: {data[3]}")
            print("------------------------")

def total_expense():
    total = 0

    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            for line in f:
                total += float(line.strip().split(",")[2])

    print("Total Expense = ₹", total)

def search_category():
    cat = input("Enter Category: ")

    found = False

    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            for line in f:
                data = line.strip().split(",")
                if data[1].lower() == cat.lower():
                    print(line.strip())
                    found = True

    if not found:
        print("No Record Found.")

while True:
    print("\n===== Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search by Category")
    print("4. Total Expense")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        search_category()
    elif choice == "4":
        total_expense()
    elif choice == "5":
        print("Thank You")
        break
    else:
        print("Invalid Choice")
