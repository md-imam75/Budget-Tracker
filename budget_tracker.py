import json
from clear_o import clear_json_file
from datetime import datetime

def add_expense(expenses, description, amount):
  expenses.append({"description": description, "amount": amount})
  
def get_total_expenses(expenses):
  sum=0
  for expense in expenses:
    sum+= expense["amount"]
  return sum  

def get_balance(budget, expenses):
  return budget - get_total_expenses(expenses)
 
def show_budget_details(budget, expenses):
  print(f"Total Budget: ${budget:.2f}")  
  print("Expenses:")
  
  for expense in expenses:
    print(f"- {expense['description']}: ${expense['amount']:.2f}")
  print(f"Remaining Budget: {get_balance(budget, expenses):.2f}")
  print(f"Total Spent: {get_total_expenses(expenses):.2f}")  

def load_budget_data(filepath):
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("Error loading data. Starting with empty data.")
        return {}

def save_budget(filepath, data):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)
        
        
def main():
    filepath = 'budget_data.json'
    data = load_budget_data(filepath)

    current_month = input("Enter month (YYYY-MM) or press Enter for current month: ")
    if not current_month:
        current_month = datetime.now().strftime("%Y-%m")

    if current_month not in data:
        initial_budget = float(input(f"Enter initial budget for {current_month}: "))
        data[current_month] = {"initial_budget": initial_budget, "expenses": []}

    else:
        initial_budget = data[current_month]["initial_budget"]

    expenses = data[current_month]["expenses"]

    while True:
        print("\nWhat would you like to do?")
        print("1. Add an expense")
        print("2. Show Budget details")
        print("3. View all months' summaries")
        print("4. Reset all data")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            description = input("Enter the description of the expense: ")
            amount = float(input("Enter the amount of the expense: "))
            add_expense(expenses, description, amount)

        elif choice == '2':
            show_budget_details(initial_budget, expenses)
        
        elif choice == '3':
          print("\n--- All Months Summary ---")
          for month, info in data.items():
            total_spent = get_total_expenses(expenses)
            balance = initial_budget - total_spent
            print(f"\n{month}")
            print(f"  - Budget: ${initial_budget:.2f}")
            print(f"  - Spent: ${total_spent:.2f}")
            print(f"  - Remaining: ${balance:.2f}")    
        elif choice == '4':
            clear_json_file(filepath)
            print("All data has been reset.")
          
        elif choice == '5':
            data[current_month]={
                "initial_budget": initial_budget,
                "expenses": expenses
            }
            save_budget(filepath, data)
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
    