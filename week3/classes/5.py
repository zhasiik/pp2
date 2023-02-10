class Bank:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, x):
        self.balance += x
    def withdraw(self, x):
        if self.balance >= x:
            self.balance -= x
x = Bank("Olzhas", 1000)

for i in range(10):
    t = int(input())
    if t == 1:
            y = int(input())
            x.deposit(y)
    else:
            y = int(input())
            x.withdraw(y)
    print(x.balance)