import csv
import os

FILE_NAME = "expenses.csv"

#  Function to initialize CSV file
def init_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount"])  # headers

#  Function to add an expense
def add_expense(date, category, amount):
    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])
    print(" Expense added successfully!")

#  Function to view all expenses
def view_expenses():
    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

#  Function to calculate total spent
def total_expenses():
    total = 0
    with open(FILE_NAME, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total += float(row["Amount"])
    print(f" Total Spent: {total}")

#  Main menu
def main():
    init_file()
    while True:
        print("\n===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category (Food/Travel/Other): ")
            amount = input("Enter amount: ")
            add_expense(date, category, amount)
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print(" Invalid choice, try again!")

if __name__ == "__main__":
    main()
