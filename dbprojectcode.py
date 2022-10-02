class Accounts(object):
    def __init__(self, name:str, amount:int):
        self.Name=name
        self.Amount = amount
        print("Account for {} created.  Balance in {}".format(self.Name, self.Amount))

    def deposit(self, amount):
        self.Amount += amount
        print("Account for {} added amount {}.  Balance in {}".format(self.Name,amount, self.Amount))

    def withdraw(self,amount):
        self.Amount -= amount
        print("Account for {} subtracted amount {}.  Balance in {}".format(self.Name,amount, self.Amount))
        if callable(self.showbalance):
            print("showbalance is callable... weee...")
            self.showbalance()

    def showbalance(self):
        print("Balance in Account for {} is {}".format(self.Name,self.Amount))

    Amount = int()
    Name =str()


Khabib = Accounts("Khabib",1000)
Khabib.deposit(1000)
Khabib.withdraw(500)
Khabib.showbalance()





