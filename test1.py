import tkinter as tk
from tkinter import messagebox

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
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(f"Insufficient funds. Available balance is {self.balance}.")
        elif amount > 0:
            self.balance -= amount
        else:
            raise ValueError("Withdrawal amount must be positive.")

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
        self.balance += interest
        return interest

class CheckingAccount(Account):
    def __init__(self, account_number, account_holder, initial_balance=0):
        super().__init__(account_number, account_holder, initial_balance)

accounts = {}

def create_account():
    account_number = entry_acc_number.get()
    account_holder = entry_acc_holder.get()
    account_type = var_account_type.get()
    initial_balance = float(entry_initial_balance.get())
    
    if account_type == "Savings":
        interest_rate = float(entry_interest_rate.get())
        accounts[account_number] = SavingsAccount(account_number, account_holder, initial_balance, interest_rate)
    elif account_type == "Checking":
        accounts[account_number] = CheckingAccount(account_number, account_holder, initial_balance)
    else:
        messagebox.showerror("Error", "Invalid account type!")
        return
    messagebox.showinfo("Success", "Account created successfully!")
    clear_entries()

def deposit_money():
    account_number = entry_acc_number.get()
    amount = float(entry_amount.get())
    if account_number in accounts:
        try:
            accounts[account_number].deposit(amount)
            messagebox.showinfo("Success", f"Deposited {amount}. New balance is {accounts[account_number].get_balance()}.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showerror("Error", "Account not found!")
    clear_entries()

def withdraw_money():
    account_number = entry_acc_number.get()
    amount = float(entry_amount.get())
    if account_number in accounts:
        try:
            accounts[account_number].withdraw(amount)
            messagebox.showinfo("Success", f"Withdrew {amount}. New balance is {accounts[account_number].get_balance()}.")
        except (ValueError, InsufficientFundsError) as e:
            messagebox.showerror("Error", str(e))
    else:
        messagebox.showerror("Error", "Account not found!")
    clear_entries()

def calculate_interest():
    account_number = entry_acc_number.get()
    if account_number in accounts:
        if isinstance(accounts[account_number], SavingsAccount):
            interest = accounts[account_number].calculate_interest()
            messagebox.showinfo("Success", f"Interest calculated: {interest}. New balance is {accounts[account_number].get_balance()}.")
        else:
            messagebox.showerror("Error", "Interest calculation is only available for savings accounts!")
    else:
        messagebox.showerror("Error", "Account not found!")
    clear_entries()

def display_account_info():
    account_number = entry_acc_number.get()
    if account_number in accounts:
        info = accounts[account_number].display_account_info()
        messagebox.showinfo("Account Info", info)
    else:
        messagebox.showerror("Error", "Account not found!")
    clear_entries()

def clear_entries():
    entry_acc_number.delete(0, tk.END)
    entry_acc_holder.delete(0, tk.END)
    entry_initial_balance.delete(0, tk.END)
    entry_interest_rate.delete(0, tk.END)
    entry_amount.delete(0, tk.END)
    var_account_type.set(None)

app = tk.Tk()
app.title("Banking System")
app.geometry("400x400")

tk.Label(app, text="Account Number:").pack()
entry_acc_number = tk.Entry(app)
entry_acc_number.pack()

tk.Label(app, text="Account Holder:").pack()
entry_acc_holder = tk.Entry(app)
entry_acc_holder.pack()

tk.Label(app, text="Account Type:").pack()
var_account_type = tk.StringVar()
tk.Radiobutton(app, text="Savings", variable=var_account_type, value="Savings").pack()
tk.Radiobutton(app, text="Checking", variable=var_account_type, value="Checking").pack()

tk.Label(app, text="Initial Balance:").pack()
entry_initial_balance = tk.Entry(app)
entry_initial_balance.pack()

tk.Label(app, text="Interest Rate (if Savings):").pack()
entry_interest_rate = tk.Entry(app)
entry_interest_rate.pack()

tk.Label(app, text="Amount (for Deposit/Withdraw):").pack()
entry_amount = tk.Entry(app)
entry_amount.pack()

tk.Button(app, text="Create Account", command=create_account).pack()
tk.Button(app, text="Deposit Money", command=deposit_money).pack()
tk.Button(app, text="Withdraw Money", command=withdraw_money).pack()
tk.Button(app, text="Calculate Interest", command=calculate_interest).pack()
tk.Button(app, text="Display Account Info", command=display_account_info).pack()

app.mainloop()
