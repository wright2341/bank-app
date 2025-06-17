class CurrentAccount:
    def __init__(self, balance=0.0, overdraft_limit=1000000.0):
        self.balance = balance
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount):
        if amount < 0:
            self.balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
        else:
            print("withdrawal exceeds overdraft limit")

    def get_balance(self):
        return self.balance