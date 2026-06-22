# Jose Reyes
# Programming Exercise 3
# This program collects monthly expenses and analyzes the total,
# highest, and lowest expense.

from functools import reduce


def get_expenses():
    # This list is needed to store each expense type and amount together.
    expenses = []

    # This input is needed so the user controls how many monthly expenses
    # they want to enter.
    number_of_expenses = int(input("How many monthly expenses do you have? "))

    # This loop is needed so the program can collect every expense from
    # the user instead of only collecting one expense.
    for expense_number in range(number_of_expenses):
        print(f"\nExpense {expense_number + 1}")

        # The expense type is needed so the highest and lowest expenses
        # can be labeled clearly in the final output.
        expense_type = input("Enter the type of expense: ")

        # The amount is needed so the program can calculate the total,
        # highest, and lowest monthly expenses.
        expense_amount = float(input("Enter the expense amount: $"))

        expenses.append({
            "type": expense_type,
            "amount": expense_amount
        })

    return expenses


def calculate_total(expenses):
    # Reduce is used here because the assignment requires the reduce method
    # to analyze the expense amounts.
    total_expense = reduce(
        lambda total, expense: total + expense["amount"],
        expenses,
        0
    )

    return total_expense


def find_highest_expense(expenses):
    # Reduce is used here to compare expenses and keep the one with
    # the highest amount.
    highest_expense = reduce(
        lambda highest, expense: expense
        if expense["amount"] > highest["amount"]
        else highest,
        expenses
    )

    return highest_expense


def find_lowest_expense(expenses):
    # Reduce is used here to compare expenses and keep the one with
    # the lowest amount.
    lowest_expense = reduce(
        lambda lowest, expense: expense
        if expense["amount"] < lowest["amount"]
        else lowest,
        expenses
    )

    return lowest_expense


def display_results(total_expense, highest_expense, lowest_expense):
    # This output is needed so the user can see the final expense analysis.
    print("\nMonthly Expense Summary")
    print(f"Total Expenses: ${total_expense:.2f}")
    print(
        f"Highest Expense: {highest_expense['type']} "
        f"(${highest_expense['amount']:.2f})"
    )
    print(
        f"Lowest Expense: {lowest_expense['type']} "
        f"(${lowest_expense['amount']:.2f})"
    )


def main():
    # The main function is used to control the order of the program.
    expenses = get_expenses()

    # These function calls are needed to calculate the required results
    # after the expense list has been created.
    total_expense = calculate_total(expenses)
    highest_expense = find_highest_expense(expenses)
    lowest_expense = find_lowest_expense(expenses)

    display_results(total_expense, highest_expense, lowest_expense)


if __name__ == "__main__":
    main()