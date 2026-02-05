# 🐍 OOPs via Python

A clean and beginner-friendly repository to understand **Object-Oriented Programming (OOPs) concepts using Python** with simple examples and real-world logic.

This repository is designed for:
- 📘 College students
- 🧠 Beginners in Python
- 💼 Interview & viva preparation
- 🚀 Strong OOP fundamentals

---

## 📌 What is OOP?

**Object-Oriented Programming (OOP)** is a programming paradigm that organizes code using **classes and objects**, making programs:
- Modular
- Reusable
- Scalable
- Easy to maintain

Python fully supports OOP concepts and also adds flexibility through features like dynamic typing and multiple inheritance.

---

## 🧩 Core OOP Concepts Covered

### 1️ Class & Object
- Blueprint (Class) and real-world entity (Object)
- Attributes and methods
- Object creation using constructors

```python
class Student:
    def __init__(self, name):
        self.name = name
```
### 2 Constructor (__init__)
- Automatically called when an object is created
- Used to initialize object data
- Executes only once per object
- Helps assign initial values to attributes

### 3 Encapsulation
- Binding data and methods together
- Data hiding using:
   - Public
   - Protected (_variable)
   - Private (__variable)
     
- Public
``` python
  class Student:
    def __init__(self, name):
        self.name = name   # public

obj = Student("Minhaj")
print(obj.name)
```
- Protected Members
   - Convention-based protection
   - Should be accessed only inside class or child class
``` python 
class Student:
    def __init__(self):
        self._roll = 101   # protected

class Child(Student):
    def show(self):
        print(self._roll)

obj = Child()
obj.show()
```
- Private Members
   - Cannot be accessed directly outside class
   - Python internally renames it (name mangling)
``` python
class Bank:
    def __init__(self):
        self.__balance = 1000

    def show_balance(self):
        print(self.__balance)

obj = Bank()
obj.show_balance() # correct
obj.__balance  # error u cant access directly this
```
### 4 Inheritance
- Inheritance allows one class to reuse properties and methods of another class.

```python
class University:
    def show(self):
        print("University Class")

class Student(University):
    pass

obj = Student()
obj.show()
```
- Types of Inheritance:
  
   - Single (One parent → One child)
```python
class Parent:
    def show_parent(self):
        print("This is Parent class")

class Child(Parent):
    def show_child(self):
        print("This is Child class")

obj = Child()
obj.show_parent()
obj.show_child()
```
   - Multilevel (Grandparent → Parent → Child)
``` python
class GrandParent:
    def show_grandparent(self):
        print("This is GrandParent class")

class Parent(GrandParent):
    def show_parent(self):
        print("This is Parent class")

class Child(Parent):
    def show_child(self):
        print("This is Child class")

obj = Child()
obj.show_grandparent()
obj.show_parent()
obj.show_child()  
```
   - Multiple (Multiple parents → One child)
```python
class Student:
    def study(self):
        print("Student is studying")

class Teacher:
    def teach(self):
        print("Teacher is teaching")

class TeachingAssistant(Student, Teacher):
    def assist(self):
        print("Teaching Assistant is assisting")

obj = TeachingAssistant()
obj.study()
obj.teach()
obj.assist()
```
   - hierarchical (One parent → Multiple children)
```python
class University:
    def show_university(self):
        print("University Class")

class Student(University):
    def show_student(self):
        print("Student Class")

class Teacher(University):
    def show_teacher(self):
        print("Teacher Class")

s = Student()
t = Teacher()

s.show_university()
s.show_student()

t.show_university()
t.show_teacher()
```
   - Hybrid (Combination of multiple inheritance types)
```python
class University:
    def show_university(self):
        print("University")

class Student(University):
    def study(self):
        print("Studying")

class Teacher(University):
    def teach(self):
        print("Teaching")

class TeachingAssistant(Student, Teacher):
    def assist(self):
        print("Assisting")

obj = TeachingAssistant()
obj.show_university()
obj.study()
obj.teach()
obj.assist()
```
### 5 Method Resolution Order (MRO)
- MRO defines the order in which Python searches for methods.
```python
class A: pass
class B(A): pass
class C(B): pass

print(C.__mro__)
```

```python
C → B → A → object
```

### 6 super() Function
- super() is used to call parent class methods
- In multiple inheritance, it follows MRO.

```python 
class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    def show(self):
        super().show()
        print("Child")

obj = Child()
obj.show()
```
### 7 *args and **kwargs
- Used to pass variable number of arguments.
- *args (multiple values)
```python
def add(*args):
    print(args)

add(1, 2, 3)
```
- **kwargs (key-value pairs)
```python
def info(**kwargs):
    print(kwargs)

info(name="Minhaj", age=21)
```
- Used heavily with super() in multiple inheritance
``` python
def __init__(self, **kwargs):
    super().__init__(**kwargs)
```
### 8 Polymorphism
 - Polymorphism means same method name, different behavior.
 - Types of Polymorphism
   
#### 1 Compile Time Polymorphism (Static / Early Binding)
- Decision taken before program runs
- ➜ Function Overloading
    - Same function name, different parameters
      
```python
class Math:
    def add(self, a, b, c=0):
        return a + b + c

m = Math()
print(m.add(2,3))
print(m.add(2,3,4))
```
- Another example
```python
class Fun:
    def fun(self, x=None, y=None):

        if x == None and y == None:
            print("Hello This is Python Polymorphism!")
            print("Thanks for Visit")

        elif x != None and y == None:
            f = 1
            for i in range(1, x+1):
                f *= i
            print(f)

        else:
            print("Addition is :", x + y)


# object creation
ob = Fun()

# different behaviours (polymorphism)
ob.fun()          # no arguments
ob.fun(5)         # one argument → factorial
ob.fun(3, 4)      # two arguments → addition
```
➜ Operator Overloading
- Same operator behaves differently for objects

```python
print(5 + 3)
print("Hello " + "World")
print([1,2] + [3,4])
```
- Other example of Operator Overlaoding
```python
class A:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other.x


ob1 = A(10)
ob2 = A(20)

print(ob1 + ob2)
```
| Method     | Called When    |
| ---------- | -------------- |
| `__init__` | object created |
| `__str__`  | print(object)  |
| `__add__`  | +              |
| `__sub__`  | -              |
| `__mul__`  | *              |
| `__len__`  | len(object)    |
| `__eq__`   | ==             |
| `__lt__`   | <              |


#### 2️ Run Time Polymorphism (Dynamic / Late Binding)
- Decision taken while program runs
➜ Method Overriding (Most Important)
- Child class changes parent class function
- 
```python
class Animal:
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

a = Dog()
a.sound()

a = Cat()
a.sound()
```

#### 3 Duck Typing (Python Special Polymorphism)
- Python checks behavior, not type
- "If it walks like a duck and quacks like a duck — it's a duck"

```python
class Bird:
    def fly(self):
        print("Bird flying")

class Airplane:
    def fly(self):
        print("Airplane flying")

for obj in (Bird(), Airplane()):
    obj.fly()
```

| Concept              | Happens In     | Key Idea                   |
| -------------------- | -------------- | -------------------------- |
| Overloading          | Same class     | Same name, diff parameters |
| Overriding           | Parent → Child | Replace behavior           |
| Operator Overloading | Objects        | +, -, *, etc               |
| Duck Typing          | Python         | Method matters, not type   |


### 9 Abstraction
- Abstraction hides implementation details and shows only essential features.

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def area(self):
        print("Area of square")
```
- Cannot create object of abstract class
- Forces child class to implement method
### 10 Destructor (__del__)
- Destructor is called when an object is destroyed.
```python
class Demo:
    def __del__(self):
        print("Object destroyed")

obj = Demo()
del obj
```
