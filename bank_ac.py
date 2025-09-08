class BankAccount:
    def __init__(self,accountnumber,accountname,balance=0):
        self.accountnumber=accountnumber
        self.accountname=accountname
        self.balance=balance

    def deposit(self,amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")

class SavingsAccount(BankAccount):
    def apply_interest(self, rate):
        self.balance += self.balance * rate/100
        print(f"New balance is {self.balance}.")



account = BankAccount("123456", "Kush Bhogate", 1000)
account.deposit(500)
account.withdraw(200)

savings = SavingsAccount("654321", "Ved Bhogate", 2000)
savings.apply_interest(5)

