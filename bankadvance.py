class InsufficientFundsError(Exception):
    """Custom exception for insufficient funds."""
    pass

class Account:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(f"Insufficient funds. Available balance is {self.balance}.")
        elif amount > 0:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance

    def display_account_info(self):
        return f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: {self.balance}"

class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, initial_balance=0, interest_rate=0.01):
        super().__init__(account_number, account_holder, initial_balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        print(f"Interest calculated: {interest}")
        self.balance += interest
        print(f"New balance after interest: {self.balance}")

class CheckingAccount(Account):
    def __init__(self, account_number, account_holder, initial_balance=0):
        super().__init__(account_number, account_holder, initial_balance)

class Transaction:
    def __init__(self, transaction_id, from_account, to_account, amount):
        self.transaction_id = transaction_id
        self.from_account = from_account
        self.to_account = to_account
        self.amount = amount

    def execute(self):
        try:
            self.from_account.withdraw(self.amount)
            self.to_account.deposit(self.amount)
            print(f"Transaction {self.transaction_id} executed successfully.")
        except InsufficientFundsError as e:
            print(f"Transaction {self.transaction_id} failed: {e}")

def main():
    accounts = {}
    while True:
        print("\nBanking System Menu")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Transfer Money")
        print("5. Calculate Interest (Savings Account)")
        print("6. Display Account Info")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            account_number = input("Enter account number: ")
            account_holder = input("Enter account holder name: ")
            account_type = input("Enter account type (savings/checking): ")
            initial_balance = float(input("Enter initial balance: "))

            if account_type.lower() == "savings":
                interest_rate = float(input("Enter interest rate (e.g., 0.01 for 1%): "))
                accounts[account_number] = SavingsAccount(account_number, account_holder, initial_balance, interest_rate)
            elif account_type.lower() == "checking":
                accounts[account_number] = CheckingAccount(account_number, account_holder, initial_balance)
            else:
                print("Invalid account type!")

        elif choice == "2":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            if account_number in accounts:
                accounts[account_number].deposit(amount)
            else:
                print("Account not found!")

        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            if account_number in accounts:
                try:
                    accounts[account_number].withdraw(amount)
                except InsufficientFundsError as e:
                    print(e)
            else:
                print("Account not found!")

        elif choice == "4":
            from_account_number = input("Enter from account number: ")
            to_account_number = input("Enter to account number: ")
            amount = float(input("Enter amount to transfer: "))
            if from_account_number in accounts and to_account_number in accounts:
                transaction = Transaction("T001", accounts[from_account_number], accounts[to_account_number], amount)
                transaction.execute()
            else:
                print("One or both accounts not found!")

        elif choice == "5":
            account_number = input("Enter account number: ")
            if account_number in accounts:
                if isinstance(accounts[account_number], SavingsAccount):
                    accounts[account_number].calculate_interest()
                else:
                    print("Interest calculation is only available for savings accounts!")
            else:
                print("Account not found!")

        elif choice == "6":
            account_number = input("Enter account number: ")
            if account_number in accounts:
                print(accounts[account_number].display_account_info())
            else:
                print("Account not found!")

        elif choice == "7":
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
