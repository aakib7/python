# ## Variables
class Car:
    wheel = 4 # static variabel(Class Variable)
    
    def __init__(self): # instance variable
        self.mil = 10
        self.company = "BMW"

car1 = Car()
car2 = Car()
print(car1.company)
print(car2.company)
car1.company = "Audi"
print("After changing car1 company.")
print(car1.company)
print(car2.company)
print("Wheels")
print(car1.wheel)
print(car2.wheel)
Car.wheel = 5
print("After Changing Wheels.")
print(car1.wheel)
print(car2.wheel)

## Methods>>>

class Student:
    school = "GOVT. High School"
    def __init__(self,name,roll):
        self.name = name
        self.rigestration_number = roll
    
    def get_name(self): # instance method(Accessor Method)
        return self.name
    
    def set_name(self,name): # Mutator method(Accessor Method)
        self.name = name
    
    @ classmethod
    def get_schoolname(cls): # work with class variable
        return cls.school
    
    @ staticmethod
    def info():
        print("Nothing to do with any Variable")
        
student1 = Student("Aakib","SP19-BSE-087")
print("Before Any Changing:")
print(student1.get_name())
print(Student.get_schoolname())
Student.info()
print("After Changing:")
student1.set_name("Ali")
Student.school = "Kips"
print(student1.get_name())
print(Student.get_schoolname())


    
    

