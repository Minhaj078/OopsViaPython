# ``` Title: Multiple Inheritance with MRO and super() in Python ```

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

# 1. Create a base class University. Derive Student and Teacher from it. 
#    Then create TeachingAssistant that inherits from both Student and Teacher 
#    and implements methods for studying, teaching, and assisting.

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


# Base class using explicit calls
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

# 2. Create a base class Vehicle. Derive Car and Boat from it. 
#    Then create AmphibiousVehicle that inherits from both Car and Boat 
#    and shows land and water transportation.


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

# av.show_Vehicle_type()
# av.Show_Car_Name()
# av.Show_Boat_Name()
# av.showTransportation()


# 3. Create a base class Device. Derive Camera and Phone from it. 
#    Then create SmartGadget that inherits from both Camera and Phone 
#    and performs multitasking operations.

class Device:
    def __init__(self,device_type):
        self.device_type = device_type

    def show_Device_type(self):
        print(f"Device type is: {self.device_type} type")

class Camera(Device):
    def __init__(self, device_type,camera_type):
        Device.__init__(self, device_type)
        self.camera_type = camera_type
    
    def show_Camera_type(self):
        print(f"Camera type is: {self.camera_type} type")

class Phone(Device):
    def __init__(self, device_type,Phone_type):
        Device.__init__(self, device_type)
        self.Phone_type = Phone_type
    
    def show_phone_type(self):
        print(f"Phone type is: {self.Phone_type} type")
    
class SmartGadget(Camera, Phone):
    def __init__(self, device_type, camera_type, Phone_type):
        Camera.__init__(self, device_type, camera_type)
        Phone.__init__(self, device_type, Phone_type)

    def showMultitasking(self):
        print(f"{self.camera_type} is used for taking pictures!")
        print(f"{self.Phone_type} is used for communication!")
sg = SmartGadget("Multitasking","DSLR","Smartphone")

sg.show_Device_type()
sg.show_Camera_type()
sg.show_phone_type()
sg.showMultitasking()

# 4. Create a base class Person. Derive Dancer and Singer from it. 
#    Then create Performer that inherits from both Dancer and Singer 
#    and performs on stage.

class Person:
    def __init__(self,PName):
        self.PName = PName
    
    def show_Pname(self):
        print(f"Person Name is: {self.PName}")

class Dancer(Person):
    def __init__(self, PName, dance_style):
        Person.__init__(self, PName)
        self.dance_style = dance_style

    def show_dance_style(self):
        print(f"Dance Style is: {self.dance_style}")

class Singer(Person):
    def __init__(self, PName, singing_style):
        Person.__init__(self, PName)
        self.singing_style = singing_style

    def show_singing_style(self):
        print(f"Singing Style is: {self.singing_style}")

class Performer(Dancer, Singer):
    def __init__(self, PName, dance_style, singing_style):
        Dancer.__init__(self, PName, dance_style)
        Singer.__init__(self, PName, singing_style)

    def show_performer_details(self):
        self.show_Pname()
        self.show_dance_style()
        self.show_singing_style()

p = Performer("John", "Ballet", "Opera")
p.show_performer_details()

# 5. Create a base class Company. Derive Programmer and Tester from it. 
#    Then create SoftwareEngineer that inherits from both Programmer and Tester 
#    and handles complete software development.

class Company:
    def __init__(self, company_name):
        self.company_name = company_name

    def show_company_name(self):
        print(f"Company Name is: {self.company_name}")

class Programmer(Company):
    def __init__(self, company_name, programming_language):
        Company.__init__(self, company_name)
        self.programming_language = programming_language

    def show_programming_language(self):
        print(f"Programming Language is: {self.programming_language}")

class Tester(Company):
    def __init__(self, company_name, testing_tool):
        Company.__init__(self, company_name)
        self.testing_tool = testing_tool

    def show_testing_tool(self):
        print(f"Testing Tool is: {self.testing_tool}")

class SoftwareEngineer(Programmer, Tester):
    def __init__(self, company_name, programming_language, testing_tool):
        Programmer.__init__(self, company_name, programming_language)
        Tester.__init__(self, company_name, testing_tool)

    def show_software_engineer_details(self):
        self.show_company_name()
        self.show_programming_language()
        self.show_testing_tool()

se = SoftwareEngineer("TechCorp", "Python", "Selenium")
se.show_software_engineer_details()


# 6. Create a base class Bank. Derive SavingsAccount and LoanAccount from it. 
#    Then create Customer that inherits from both SavingsAccount and LoanAccount 
#    and manages finances.

class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name

    def show_bank_name(self):
        print(f"Bank Name is: {self.bank_name}")

class SavingsAccount(Bank):
    def __init__(self, bank_name, savings_balance):
        Bank.__init__(self, bank_name)
        self.savings_balance = savings_balance

    def show_savings_balance(self):
        print(f"Savings Balance is: {self.savings_balance}")

class LoanAccount(Bank):
    def __init__(self, bank_name, loan_amount):
        Bank.__init__(self, bank_name)
        self.loan_amount = loan_amount

    def show_loan_amount(self):
        print(f"Loan Amount is: {self.loan_amount}")

class Customer(SavingsAccount, LoanAccount):
    def __init__(self, bank_name, savings_balance, loan_amount):
        SavingsAccount.__init__(self, bank_name, savings_balance)
        LoanAccount.__init__(self, bank_name, loan_amount)

    def show_customer_finances(self):
        self.show_bank_name()
        self.show_savings_balance()
        self.show_loan_amount()

c = Customer("FinanceBank", 10000, 5000)
c.show_customer_finances()


# 7. Create a base class Media. Derive Audio and Video from it. 
#    Then create Multimedia that inherits from both Audio and Video 
#    and plays all types of media.

class Media:
    def __init__(self, media_type):
        self.media_type = media_type

    def show_media_type(self):
        print(f"Media Type is: {self.media_type}")

class Audio(Media):
    def __init__(self, media_type, audio_format):
        Media.__init__(self, media_type)
        self.audio_format = audio_format

    def show_audio_format(self):
        print(f"Audio Format is: {self.audio_format}")

class Video(Media):
    def __init__(self, media_type, video_format):
        Media.__init__(self, media_type)
        self.video_format = video_format

    def show_video_format(self):
        print(f"Video Format is: {self.video_format}")

class Multimedia(Audio, Video):
    def __init__(self, media_type, audio_format, video_format):
        Audio.__init__(self, media_type, audio_format)
        Video.__init__(self, media_type, video_format)

    def show_multimedia_details(self):
        self.show_media_type()
        self.show_audio_format()
        self.show_video_format()

mm = Multimedia("Multimedia", "MP3", "MP4")
mm.show_multimedia_details()


# 8. Create a base class School. Derive SportsStudent and MusicStudent from it. 
#    Then create AllRounder that inherits from both SportsStudent and MusicStudent 
#    and performs multiple talents.

class School:
    def __init__(self, school_name):
        self.school_name = school_name

    def show_school_name(self):
        print(f"School Name is: {self.school_name}")

class SportsStudent(School):
    def __init__(self, school_name, sport):
        School.__init__(self, school_name)
        self.sport = sport

    def show_sport(self):
        print(f"Sport is: {self.sport}")

class MusicStudent(School):
    def __init__(self, school_name, instrument):
        School.__init__(self, school_name)
        self.instrument = instrument

    def show_instrument(self):
        print(f"Instrument is: {self.instrument}")

class AllRounder(SportsStudent, MusicStudent):
    def __init__(self, school_name, sport, instrument):
        SportsStudent.__init__(self, school_name, sport)
        MusicStudent.__init__(self, school_name, instrument)

    def show_allrounder_details(self):
        self.show_school_name()
        self.show_sport()
        self.show_instrument()

ar = AllRounder("Greenwood High", "Football", "Piano")
ar.show_allrounder_details()


# 9. Create a base class OnlinePlatform. Derive Buyer and Seller from it. 
#    Then create MarketplaceUser that inherits from both Buyer and Seller 
#    and performs trading.

class OnlinePlatform:
    def __init__(self, platform_name):
        self.platform_name = platform_name

    def show_platform_name(self):
        print(f"Platform Name is: {self.platform_name}")

class Buyer(OnlinePlatform):
    def __init__(self, platform_name, buyer_name):
        OnlinePlatform.__init__(self, platform_name)
        self.buyer_name = buyer_name

    def show_buyer_name(self):
        print(f"Buyer Name is: {self.buyer_name}")

class Seller(OnlinePlatform):
    def __init__(self, platform_name, seller_name):
        OnlinePlatform.__init__(self, platform_name)
        self.seller_name = seller_name

    def show_seller_name(self):
        print(f"Seller Name is: {self.seller_name}")

class Marketplace:
    def __init__(self, platform_name, buyer_name, seller_name):
        Buyer.__init__(self, platform_name, buyer_name)
        Seller.__init__(self, platform_name, seller_name)

    def show_marketplace_user_details(self):
        self.show_platform_name()
        self.show_buyer_name()
        self.show_seller_name()

mu = Marketplace("ShopEasy", "Alice", "Bob")
mu.show_marketplace_user_details()

# 10. Create a base class Transport. Derive BusService and TrainService from it. 
#     Then create SmartTransport that inherits from both BusService and TrainService 
#     and controls both services.

class Transport:
    def __init__(self, transport_type):
        self.transport_type = transport_type

    def show_transport_type(self):
        print(f"Transport Type is: {self.transport_type}")

class BusService(Transport):
    def __init__(self, transport_type, bus_number):
        Transport.__init__(self, transport_type)
        self.bus_number = bus_number

    def show_bus_number(self):
        print(f"Bus Number is: {self.bus_number}")

class TrainService(Transport):
    def __init__(self, transport_type, train_number):
        Transport.__init__(self, transport_type)
        self.train_number = train_number

    def show_train_number(self):
        print(f"Train Number is: {self.train_number}")

class SmartTransport(BusService, TrainService):
    def __init__(self, transport_type, bus_number, train_number):
        BusService.__init__(self, transport_type, bus_number)
        TrainService.__init__(self, transport_type, train_number)

    def show_smart_transport_details(self):
        self.show_transport_type()
        self.show_bus_number()
        self.show_train_number()

st = SmartTransport("Public", "B123", "T456")
st.show_smart_transport_details()
