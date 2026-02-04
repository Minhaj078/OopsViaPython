# ENCAPSULATION OOP PRACTICE QUESTIONS

# 1. Create a Student class where marks are private and accessed using getter method.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks  # private attribute

    def get_marks(self):
        return self.__marks
    
# Example usage
student = Student("Alice", 85)
print(f"{student.name}'s marks: {student.get_marks()}")


# 2. Create a BankAccount class with private balance and methods to deposit and check balance.

class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.__balance = initial_balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")

    def get_balance(self):
        return self.__balance

# Example usage
account = BankAccount("Bob", 100)
account.deposit(50)
print(f"{account.account_holder}'s balance: {account.get_balance()}")

# 3. Create a Person class where age is private and cannot be negative.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = 0  # private attribute
        self.set_age(age)

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Age cannot be negative.")

    def get_age(self):
        return self.__age
    
# Example usage
person = Person("Charlie", 25)
print(f"{person.name}'s age: {person.get_age()}")
person.set_age(-5)  # Attempt to set negative age
print(f"{person.name}'s age after invalid update: {person.get_age()}")

# 4. Create a User class that hides password and verifies it using a method.

class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  # private attribute

    def verify_password(self, password):
        return self.__password == password  
    
# Example usage
user = User
("dave", "secure123")
print(f"Password verification for dave: {user.verify_password('secure123')}")
print(f"Password verification for dave: {user.verify_password('wrongpass')}")

# 5. Create an Employee class where salary is private and can be increased.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # private attribute

    def increase_salary(self, amount):
        if amount > 0:
            self.__salary += amount
            print(f"Salary increased by: {amount}")
        else:
            print("Increase amount must be positive.")

    def get_salary(self):
        return self.__salary
    
# Example usage
employee = Employee("Eve", 50000)
employee.increase_salary(5000)
print(f"{employee.name}'s salary: {employee.get_salary()}")

# 6. Create a Car class with private speed and methods accelerate and brake.

class Car:
    def __init__(self, model):
        self.model = model
        self.__speed = 0  # private attribute

    def accelerate(self, increment):
        if increment > 0:
            self.__speed += increment
            print(f"Accelerated by: {increment}")
        else:
            print("Increment must be positive.")

    def brake(self, decrement):
        if decrement > 0 and self.__speed - decrement >= 0:
            self.__speed -= decrement
            print(f"Braked by: {decrement}")
        else:
            print("Decrement must be positive and cannot reduce speed below zero.")

    def get_speed(self):
        return self.__speed
    
# Example usage
car = Car("Tesla Model S")
car.accelerate(30)
car.brake(10)
print(f"Current speed: {car.get_speed()}")

# 7. Create a Mobile class where battery percentage is private and decreases when used.

class Mobile:
    def __init__(self, brand):
        self.brand = brand
        self.__battery_percentage = 100  # private attribute

    def use(self, hours):
        consumption = hours * 10  # assuming 10% battery consumption per hour
        if consumption <= self.__battery_percentage:
            self.__battery_percentage -= consumption
            print(f"Used for {hours} hours. Battery decreased by {consumption}%.")
        else:
            print("Not enough battery to use for that long.")

    def get_battery_percentage(self):
        return self.__battery_percentage
    
# Example usage
mobile = Mobile("Samsung")
mobile.use(3)
print(f"{mobile.brand} battery percentage: {mobile.get_battery_percentage()}%")

# 8. Create an ATM class with hidden PIN and verification method.

class ATM:
    def __init__(self, card_holder, pin):
        self.card_holder = card_holder
        self.__pin = pin  # private attribute

    def verify_pin(self, pin):
        return self.__pin == pin
    
# Example usage
atm = ATM("Frank", "1234")
print(f"PIN verification for Frank: {atm.verify_pin('1234')}")
print(f"PIN verification for Frank: {atm.verify_pin('0000')}")


# 9. Create a Book class where price is private and cannot be negative.

class Book:
    def __init__(self, title, price):
        self.title = title
        self.__price = 0  # private attribute
        self.set_price(price)

    def set_price(self, price):
        if price >= 0:
            self.__price = price
        else:
            print("Price cannot be negative.")

    def get_price(self):
        return self.__price
    
# Example usage
book = Book("Python Programming", 29.99)
print(f"Book: {book.title}, Price: {book.get_price()}")
book.set_price(-10)  # Attempt to set negative price
print(f"Book: {book.title}, Price after invalid update: {book.get_price()}")

# 10. Create a Result class where marks list is private and modified using methods.
class Result:
    def __init__(self, student_name):
        self.student_name = student_name
        self.__marks = []  # private attribute

    def add_mark(self, mark):
        if 0 <= mark <= 100:
            self.__marks.append(mark)
            print(f"Added mark: {mark}")
        else:
            print("Mark must be between 0 and 100.")

    def get_marks(self):
        return self.__marks
    
# Example usage
result = Result("Grace")
result.add_mark(95)
result.add_mark(85)
print(f"Student: {result.student_name}, Marks: {result.get_marks()}")
