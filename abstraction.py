# ABSTRACTION OOPS PRACTICE QUESTIONS IN PYTHON

# 1. Create an abstract class Animal with abstract method sound() and implement it in Dog class.

from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        return "Bark"
    
dog = Dog()
print(dog.sound())

# 2. Create an abstract class Shape with abstract method area() and implement it in Rectangle class.

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
rect = Rectangle(5, 10)
print(rect.area())

# 3. Create an abstract class Bank with abstract method interest_rate() and implement it in SBI class.

class Bank(ABC):
    @abstractmethod
    def interest_rate(self):
        pass
class SBI(Bank):
    def interest_rate(self):
        return 7.5
sbi = SBI()
print(sbi.interest_rate())

# 4. Create an abstract class Vehicle with abstract method speed() and implement it in Car class.

class Vehicle(ABC):
    @abstractmethod
    def speed(self):
        pass
class Car(Vehicle):
    def speed(self):
        return "200 Kmph"

# 5. Create an abstract class Employee with abstract method salary() and implement it in Developer class.

class Employee(ABC):
    @abstractmethod
    def salary(self):
        pass

class Developer(Employee):
    def salary(self):
        return  50000


# 6. Create an abstract class Payment with abstract method pay(amount) and implement it in UPI class.

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class UPI(Payment):
    def pay(self, amount):
        return f"Paid {amount} using UPI"   

# 7. Create an abstract class Mobile with abstract method features() and implement it in Samsung class.

class Mobile(ABC):
    @abstractmethod
    def features(self):
        pass
class Samsung(Mobile):
    def features(self):
        return "5G, Amoled Display, 108MP Camera"
    

# 8. Create an abstract class Course with abstract method duration() and implement it in PythonCourse class.

class Course(ABC):
    @abstractmethod
    def duration(self):
        pass

class PythonCourse(Course):
    def duration(self):
        return "5hours"
    

# 9. Create an abstract class Food with abstract method price() and implement it in Pizza class.

class Food(ABC):
    @abstractmethod
    def price(self):
        pass

class Pizza(Food):
    def price(self):
        return 10000

# 10. Create an abstract class Electronics with abstract method warranty() and implement it in Laptop class.

class Electronic(ABC):
    @abstractmethod
    def warranty(self):
        pass
class Laptop(Electronic):
    def warranty(self):
        return "5years Warranty"
