# ## Build a Bank Application

# #### **Objective:**
# Develop a command-line banking application that allows users to perform basic banking operations like creating an account, depositing money, and withdrawing money. This will help you practice using object-oriented programming (OOP), file handling, and error handling in Python.


# ### **Tasks:**

# #### **Step 1: Define the Classes**
# 1. Create a class `Account` with attributes:
#    - `account_number`
#    - `name`
#    - `balance`

# 2. Create a class `Bank` to manage all accounts. It should have:
#    - A dictionary to store accounts (`accounts`).
#    - Methods for each operation:
#      - `create_account(name, initial_deposit)`
#      - `view_account(account_number)`
#      - `deposit(account_number, amount)`
#      - `withdraw(account_number, amount)`
#      - `save_to_file()` and `load_from_file()` (for file handling).

# #### **Step 2: Implement the Methods**
# 1. **Account Creation**
#    - Generate a unique `account_number`.
#    - Create an `Account` object and store it in the dictionary.
#    - Save account details to a file.

# 2. **View Account Details**
#    - Prompt the user to input their account number.
#    - Retrieve and display the account details if found; otherwise, show an error.

# 3. **Deposit Money**
#    - Prompt the user for their account number and deposit amount.
#    - Validate the amount and update the account balance.

# 4. **Withdraw Money**
#    - Prompt the user for their account number and withdrawal amount.
#    - Validate that the amount is less than or equal to the balance and update the account balance.

# 5. **File Handling**
#    - Use `save_to_file` to write account details to `accounts.txt`.
#    - Use `load_from_file` to load account details when the program starts.

# ---


import json
import os
import random

class Account:
    def __init__(self, account_number, name, password, balance=0):
        self.account_number = account_number
        self.name = name
        self.password = password  # Store as plain text or use a simple transformation
        self.balance = balance
    
    def verify_password(self, password):
        return self.password == password  # Simple comparison
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False
    
    def to_dict(self):
        return {"account_number": self.account_number, "name": self.name, "password": self.password, "balance": self.balance}

class Bank:
    def __init__(self, filename="accounts.json"):
        self.accounts = {}
        self.filename = filename
        self.load_from_file()
    
    def generate_account_number(self):
        return str(random.randint(100, 999))
    
    def create_account(self, name, password, initial_deposit):
        if initial_deposit < 0:
            print("Initial deposit cannot be negative.")
            return None
        account_number = self.generate_account_number()
        while account_number in self.accounts:
            account_number = self.generate_account_number()
        self.accounts[account_number] = Account(account_number, name, password, initial_deposit)
        self.save_to_file()
        return account_number
    
    def authenticate(self, account_number, password):
        account = self.accounts.get(account_number)
        if account and account.verify_password(password):
            return account
        return None
    
    def view_account(self, account_number, password):
        account = self.authenticate(account_number, password)
        if account:
            return f"Account Number: {account.account_number}\nName: {account.name}\nBalance: ${account.balance:.2f}"
        return "Invalid account number or password."
    
    def deposit(self, account_number, password, amount):
        account = self.authenticate(account_number, password)
        if account and account.deposit(amount):
            self.save_to_file()
            return f"Deposit successful. New Balance: ${account.balance:.2f}"
        return "Invalid account, password, or amount."
    
    def withdraw(self, account_number, password, amount):
        account = self.authenticate(account_number, password)
        if account and account.withdraw(amount):
            self.save_to_file()
            return f"Withdrawal successful. New Balance: ${account.balance:.2f}"
        return "Invalid account, password, or insufficient balance."
    
    def save_to_file(self):
        with open(self.filename, "w") as file:
            json.dump({acc: self.accounts[acc].to_dict() for acc in self.accounts}, file, indent=4)
    
    def load_from_file(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                try:
                    data = json.load(file)
                    self.accounts = {acc: Account(**details) for acc, details in data.items()}
                except json.JSONDecodeError:
                    self.accounts = {}

def main():
    bank = Bank()
    while True:
        print("\n--- Welcome to Secure Bank ---")
        print("1. Create Account")
        print("2. View Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter your name: ")
            password = input("Set a password: ")
            try:
                initial_deposit = float(input("Enter initial deposit: "))
                account_number = bank.create_account(name, password, initial_deposit)
                if account_number:
                    print(f"Account created successfully! Your account number is {account_number}")
            except ValueError:
                print("Invalid amount. Please enter a number.")
        
        elif choice == "2":
            acc_number = input("Enter your account number: ")
            password = input("Enter your password: ")
            print(bank.view_account(acc_number, password))
        
        elif choice == "3":
            acc_number = input("Enter your account number: ")
            password = input("Enter your password: ")
            try:
                amount = float(input("Enter deposit amount: "))
                print(bank.deposit(acc_number, password, amount))
            except ValueError:
                print("Invalid amount. Please enter a number.")
        
        elif choice == "4":
            acc_number = input("Enter your account number: ")
            password = input("Enter your password: ")
            try:
                amount = float(input("Enter withdrawal amount: "))
                print(bank.withdraw(acc_number, password, amount))
            except ValueError:
                print("Invalid amount. Please enter a number.")
        
        elif choice == "5":
            print("Thank you for using Secure Bank! Goodbye.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
