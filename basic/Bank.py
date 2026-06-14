class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def create_account(self, account_number, initial_balance=0):
        if account_number in self.accounts:
            print(f"Account {account_number} already exists.")
        else:
            self.accounts[account_number] = initial_balance
            print(f"Account {account_number} created with balance {initial_balance}.")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number] += amount
            print(f"Deposited {amount} to account {account_number}. New balance: {self.accounts[account_number]}")
        else:
            print(f"Account {account_number} does not exist.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number] >= amount:
                self.accounts[account_number] -= amount
                print(f"Withdrew {amount} from account {account_number}. New balance: {self.accounts[account_number]}")
            else:
                print(f"Insufficient funds in account {account_number}. Current balance: {self.accounts[account_number]}")
        else:
            print(f"Account {account_number} does not exist.")

    def get_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            print(f"Account {account_number} does not exist.")
            return None
        

acc1 = Bank("My Bank")
acc1.create_account("12345", 1000)
acc1.deposit("12345", 500)
print(f"Balance for account 12345: {acc1.get_balance('12345')}")
acc1.withdraw("12345", 200)
acc1.get_balance("12345")
