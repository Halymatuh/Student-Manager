# Student Task and Expense Manager

# List for assignments
assignments = []

# List for expenses (item, amount)
expenses = []


# ---------------- TASK FUNCTIONS ----------------

def add_assignment():
    task = input("Enter assignment name: ")
    assignments.append({"task": task, "completed": False})
    print("Assignment added!")


def view_assignments():
    if len(assignments) == 0:
        print("No assignments found.")
    else:
        print("\nAssignments:")
        for i, assignment in enumerate(assignments):
            status = "Done" if assignment["completed"] else "Not Done"
            print(f"{i + 1}. {assignment['task']} - {status}")


def mark_completed():
    view_assignments()
    if len(assignments) > 0:
        num = int(input("Enter assignment number to mark as completed: "))
        assignments[num - 1]["completed"] = True
        print("Assignment marked as completed!")


def update_assignment():
    view_assignments()
    if len(assignments) > 0:
        num = int(input("Enter assignment number to update: "))
        new_task = input("Enter new assignment name: ")
        assignments[num - 1]["task"] = new_task
        print("Assignment updated!")


def remove_assignment():
    view_assignments()
    if len(assignments) > 0:
        num = int(input("Enter assignment number to remove: "))
        assignments.pop(num - 1)
        print("Assignment removed!")


# ---------------- EXPENSE FUNCTIONS ----------------

def add_expense():
    item = input("Enter expense item: ")
    category = input("Enter category (Lunch, Transport, Books): ")
    amount = float(input("Enter amount spent: "))

    expenses.append((item, category, amount))
    print("Expense added!")


def view_expenses():
    if len(expenses) == 0:
        print("No expenses recorded.")
    else:
        print("\nExpenses:")
        for expense in expenses:
            print(expense)

        total = sum(expense[2] for expense in expenses)
        print("Total Expenses:", total)


def filter_by_category():
    category = input("Enter category to search: ")

    filtered = [expense for expense in expenses if expense[1].lower() == category.lower()]

    print("\nMatching Expenses:")
    for expense in filtered:
        print(expense)


def expenses_above_amount():
    amount = float(input("Show expenses above: "))

    filtered = [expense for expense in expenses if expense[2] > amount]

    print("\nExpenses Above Amount:")
    for expense in filtered:
        print(expense)


# ---------------- MAIN MENU ----------------

while True:
    print("\n===== STUDENT MANAGER =====")
    print("1. Add Assignment")
    print("2. View Assignments")
    print("3. Mark Assignment Completed")
    print("4. Update Assignment")
    print("5. Remove Assignment")
    print("6. Add Expense")
    print("7. View Expenses")
    print("8. Filter Expenses by Category")
    print("9. Show Expenses Above Amount")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_assignment()
    elif choice == "2":
        view_assignments()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        update_assignment()
    elif choice == "5":
        remove_assignment()
    elif choice == "6":
        add_expense()
    elif choice == "7":
        view_expenses()
    elif choice == "8":
        filter_by_category()
    elif choice == "9":
        expenses_above_amount()
    elif choice == "0":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
