class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize account with an optional starting balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add amount to the account balance."""
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw amount if funds are sufficient."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        elif amount > self.account_balance:
            return False
        else:
            self.account_balance -= amount
            return True

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.account_balance}")
