
class Bank:
    bank_name = 'ABC'

    def __init__(self,account_number,account_balance=10000):
        self.account_balance = account_balance
        self.account_number = account_number

    def check_balance(self):
        return self.account_balance

    @staticmethod
    def do_calculation(amt,Balance):
        if amt > Balance:
            return "Insufficient Balance"
        else:
            Balance -= amt
            return Balance
        
        
    def credit_amount(self,account_number,amount):
        self.account_balance += amount
        return self.check_balance()

    def debit_amount(self,account_number,amount):
        get_result= self.do_calculation(amount,self.account_balance)
        return get_result

    def change_bankname(cls):
        cls.bank_name = 'XYZ'
        return cls.bank_name



# c1 = Bank('11111')
# print(c1.credit_amount('11111',150))
# print(c1.debit_amount('11111',50000))



from abc import ABC,abstractmethod


class Employee(ABC):
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    @abstractmethod
    def calculate_salary(self):
        pass


class FullTime(Employee):
    def calculate_salary(self):
        return self.salary

class PartTime(Employee):
    def calculate_salary(self):
        return self.salary*0.75

class ContractBases(Employee):
    def calculate_salary(self):
        return self.salary*0.5


# p1 = PartTime("vj",100000)
# print(p1.calculate_salary())




from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class SMSNotification(Notification): 
    def send(self, message):
        print(f"Sending SMS: {message}")

class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending Email: {message}")

class PushNotification(Notification):
    def send(self, message):
        print(f"Sending Push Notification: {message}")

# Sending different types of notifications
sms = SMSNotification()
sms.send("Your OTP is 1234")  # Output: Sending SMS: Your OTP is 1234

email = EmailNotification()
email.send("Welcome to our service!")  # Output: Sending Email: Welcome to our service!



from abc import ABC, abstractmethod

class Beverage(ABC):
    """Abstract class for all beverages"""
    @abstractmethod
    def ingredients(self):
        pass

class Espresso(Beverage):
    def ingredients(self):
        return {"water": 50, "coffee": 18, "milk": 0}

class Cappuccino(Beverage):
    def ingredients(self):
        return {"water": 50, "coffee": 18, "milk": 30}

class Latte(Beverage):
    def ingredients(self):
        return {"water": 50, "coffee": 18, "milk": 50}

class CoffeeMachine:
    def __init__(self):
        self.water = 500  # Initial water in ml
        self.milk = 300   # Initial milk in ml
        self.coffee = 100  # Initial coffee in grams
        self.cleaning_counter = 0  # Tracks number of drinks made

    def check_ingredients(self, beverage):
        required = beverage.ingredients()
        return (
            self.water >= required["water"] and
            self.milk >= required["milk"] and
            self.coffee >= required["coffee"]
        )

    def make_coffee(self, beverage):
        if not self.check_ingredients(beverage):
            print("Not enough ingredients! Please refill.")
            return
        
        # Deduct ingredients
        required = beverage.ingredients()
        self.water -= required["water"]
        self.milk -= required["milk"]
        self.coffee -= required["coffee"]
        self.cleaning_counter += 1

        print(f"Your {beverage.__class__.__name__} is ready! ☕")
        self.check_maintenance()

    def refill(self, water=500, milk=300, coffee=100):
        """Refills ingredients"""
        self.water += water
        self.milk += milk
        self.coffee += coffee
        print("Ingredients refilled!")

    def check_maintenance(self):
        """Check if cleaning is needed after every 5 drinks"""
        if self.cleaning_counter >= 5:
            print("⚠️ Machine requires cleaning! Run the cleaning cycle.")
            self.cleaning_counter = 0  # Reset counter after cleaning

# Usage
machine = CoffeeMachine()

# Make different coffee types
machine.make_coffee(Espresso())   # Your Espresso is ready! ☕
machine.make_coffee(Cappuccino()) # Your Cappuccino is ready! ☕
machine.make_coffee(Latte())      # Your Latte is ready! ☕

# Simulate ingredient shortage
machine.water = 10  # Reducing water to trigger refill warning
machine.make_coffee(Espresso())   # Not enough ingredients! Please refill.

# Refill ingredients
machine.refill()  # Ingredients refilled!

# Trigger cleaning after multiple uses
for _ in range(5):
    machine.make_coffee(Espresso())  
# ⚠️ Machine requires cleaning!
