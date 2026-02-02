``` Title: Multiple Inheritance with MRO and super() in Python ```

# 1. Create a base class University. Derive Student and Teacher from it. 

#    Then create TeachingAssistant that inherits from both Student and Teacher 

#    and implements methods for studying, teaching, and assisting.

# Base class
class University:
    def __init__(self, university_name):
        self.university_name = university_name

    def show_university(self):
        print(f"University: {self.university_name}")


# Derived class 1
class Student(University):
    def __init__(self, university_name, student_name):
        University.__init__(self, university_name)   # explicit call
        self.student_name = student_name

    def study(self):
        print(f"{self.student_name} is studying.")


# Derived class 2
class Teacher(University):
    def __init__(self, university_name, teacher_name):
        University.__init__(self, university_name)   # explicit call
        self.teacher_name = teacher_name

    def teach(self):
        print(f"{self.teacher_name} is teaching.")


# Multiple inheritance
class TeachingAssistant(Student, Teacher):
    def __init__(self, university_name, student_name, teacher_name):
        Student.__init__(self, university_name, student_name)
        Teacher.__init__(self, university_name, teacher_name)

    def assist(self):
        print(f"{self.student_name} is assisting {self.teacher_name}.")

# ta = TeachingAssistant(
#     "Lovely Professional University",
#     "Minhaj",
#     "Rakesh Thakur"
# )

# ta.show_university()
# ta.study()
# ta.teach()
# ta.assist()

"""
MRO = Method Resolution Order

MRO Order:
TeachingAssistant
→ Student
→ Teacher
→ University
→ object

MRO defines the order of method calls in multiple inheritance, and **kwargs allows cooperative initialization by passing unused arguments to the next class

Multiple inheritance + super()
= MRO + **kwargs

"""


# Base class
class University:
    def __init__(self, university_name, **kwargs):
        self.university_name = university_name
        super().__init__(**kwargs)

    def show_university(self):
        print(f"University: {self.university_name}")


# Derived class 1
class Student(University):
    def __init__(self, student_name, **kwargs):
        self.student_name = student_name
        super().__init__(**kwargs)

    def study(self):
        print(f"{self.student_name} is studying.")


# Derived class 2
class Teacher(University):
    def __init__(self, teacher_name, **kwargs):
        self.teacher_name = teacher_name
        super().__init__(**kwargs)

    def teach(self):
        print(f"{self.teacher_name} is teaching.")


# Multiple inheritance
class TeachingAssistant(Student, Teacher):
    def __init__(self, university_name, student_name, teacher_name):
        super().__init__(
            university_name=university_name,
            student_name=student_name,
            teacher_name=teacher_name
        )

    def assist(self):
        print(f"{self.student_name} is assisting {self.teacher_name}.")

# ta = TeachingAssistant(
#     "Lovely Professional University",
#     "Minhaj",
#     "Rakesh Thakur"
# )

# ta.show_university()
# ta.study()
# ta.teach()
# ta.assist()

class Vehicle:
    def __init__(self,vehicle_type):
        self.vehicle_type = vehicle_type
    
    def show_Vehicle_type(self):
        print(f"Vehicle type is: {self.vehicle_type} type")

class Car(Vehicle):
    def __init__(self, vehicle_type, carName):
        Vehicle.__init__(self,vehicle_type)
        self.carName = carName

    def Show_Car_Name(self):
        print(f"Car Name is: {self.carName}")

class Boat(Vehicle):
    def __init__(self, vehicle_type, boatName):
        Vehicle.__init__(self, vehicle_type)
        self.boatName = boatName

    def Show_Boat_Name(self):
        print(f"Boat Name is: {self.boatName}")

class AmphibiousVehicle(Car, Boat):
    def __init__(self, vehicle_type, carName, boatName):
        Car.__init__(self, vehicle_type, carName)
        Boat.__init__(self, vehicle_type, boatName)

    def showTransportation(self):
        print(f"{self.carName} is used for Land Transportation!")
        print(f"{self.boatName} is used for Water Transportation!")

av = AmphibiousVehicle("Land","SUV","Avalon")
av.show_Vehicle_type()
av.Show_Car_Name()
av.Show_Boat_Name()
av.showTransportation()
