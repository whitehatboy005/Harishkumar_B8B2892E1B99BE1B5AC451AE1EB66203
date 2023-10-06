class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        self.__account_balance += amount

    def withdraw(self, amount):
        if amount <= self.__account_balance:
            self.__account_balance -= amount
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print("Account Number:", self.__account_number)
        print("Account Holder Name:", self.__account_holder_name)
        print("Account Balance:", self.__account_balance)


# Create an instance of the BankAccount class
account = BankAccount("123456789", "John Doe", 1000)

# Test deposit functionality
account.deposit(500)
account.display_balance()

# Test withdrawal functionality
account.withdraw(200)
account.display_balance()
