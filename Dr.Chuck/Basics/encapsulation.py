class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount
        
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("There is not enough balance in your account")
    def get_balance(self):
        return self.__balance
    
account = BankAccount("123456", 1000)
account.deposit(0)
account.withdraw(int(input("Enter amount: ")))
print(account.get_balance())