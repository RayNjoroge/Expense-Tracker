# Class defining an expense
class Expense:
    def __init__(self, date, description, amount):
        self.date = date
        self.description = description
        self.amount = amount

# Class with functions of the tracker
class ExpenseTracker:
    def __init__(self):
        self.expenses = []
    
    # Func to add expense
    def add_expense(self, expense):
        self.expenses.append(expense)
    
    # Func to remove an expense
    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
            print("Expense removed successfully.")
        else:
            print("Invalid expense index.")
    
    # Viewing expenses
    def view_expenses(self):
        if len(self.expenses) == 0:
            print("No expenses found!")
        else:
            print("Expense List: ")
            
            for i, expense in enumerate(self.expenses, start=1):
                print(f"{i}. Date: {expense.date}, Description: {expense.description}, Amount: Ksh{expense.amount:.2f}")

# Viewing total expenses
    def total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"Total Expenses: Ksh{total:.2f}")

def main():
    tracker = ExpenseTracker()
    
    while True:
        print("\nExpense Tracker Menu: ")
        print("\n1. Add Expense")
        print("\n2. Remove Expense")
        print("\n3. View Expenses ")
        print("\n4. Total Expenses ")
        print("\n5. Exit")
        
        choice = input("Please enter your choice between (1-5): ")
        
        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            description = input("Enter the description: ")
            amount = float(input("Enter the amount: "))
            expense = Expense(date, description, amount)
            tracker.add_expense(expense)
            print("Expense added successfully😊!")
        elif choice == "2":
            index = int(input("Enter the expense index to remove: ")) - 1
            tracker.remove_expense(index)
        elif choice == "3":
            tracker.view_expenses()
        elif choice == "4":
            tracker.total_expenses()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice ☹. Please Try Again!")
if __name__ == "__main__":
    main()