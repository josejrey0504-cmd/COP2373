# This class keeps all of the information and behaviors for a bank account
# together so they can be reused throughout the program.
class BankAcct:

    # Store the information that every bank account needs when it is created.
    def __init__(self, name, account_number, amount, interest_rate):
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

    # Allow the interest rate to be updated without creating a new account.
    def adjust_interest_rate(self, new_rate):
        self.interest_rate = new_rate

    # Increase the account balance when money is added to the account.
    def deposit(self, amount):
        self.amount += amount

    # Prevent the balance from becoming negative by checking that
    # enough money is available before removing funds.
    def withdraw(self, amount):
        if amount <= self.amount:
            self.amount -= amount
        else:
            print("Insufficient funds.")

    # Return the current balance so other parts of the program
    # can use or display it when needed.
    def get_balance(self):
        return self.amount

    # Calculate the amount of interest earned based on the
    # current balance, interest rate, and number of days.
    def calculate_interest(self, days):
        interest = self.amount * (self.interest_rate / 100) * (days / 365)
        return interest

    # Return a formatted string so the account information
    # can be displayed neatly whenever the object is printed.
    def __str__(self):
        return (
            f"Account Holder: {self.name}\n"
            f"Account Number: {self.account_number}\n"
            f"Balance: ${self.amount:.2f}\n"
            f"Interest Rate: {self.interest_rate:.2f}%"
        )


# Test each method in the class to verify that it works correctly.
def test_bank_account():

    # Create a sample account so every method can be demonstrated.
    account = BankAcct("Jose Reyes", "123456789", 1000.00, 4.5)

    # Display the account information before making any changes
    # so the user can compare the results.
    print("Original Account")
    print(account)

    # Deposit money to verify that the balance increases correctly.
    account.deposit(500)
    print("\nAfter Deposit")
    print(account)

    # Withdraw money to verify that the balance decreases correctly.
    account.withdraw(200)
    print("\nAfter Withdrawal")
    print(account)

    # Display the balance to confirm that deposits and withdrawals
    # updated the account correctly.
    print(f"\nCurrent Balance: ${account.get_balance():.2f}")

    # Change the interest rate to verify that the new rate is stored.
    account.adjust_interest_rate(5.0)
    print("\nAfter Changing Interest Rate")
    print(account)

    # Calculate the interest for 30 days and display the result
    # so the calculation can be verified.
    interest = account.calculate_interest(30)
    print(f"\nInterest Earned for 30 Days: ${interest:.2f}")


# Call the test function to start the program.
test_bank_account()