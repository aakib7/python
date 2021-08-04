class Student:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
        self.l1 = self.Laptop('HP','i5','8gb')
        
    def show(self):
        print(self.name, self.roll)
        self.l1.show()
    
    class Laptop:
        
        def __init__(self,comp,cup,ram):
            self.company = comp
            self.cup = cup
            self.ram = ram
        
        def show(self):
            print(self.company, self.cup, self.ram)
        
s1 = Student("Aakib","SP19-BSE-087")
s1.show()
# s1.l1.show()
# l2 = Student.Laptop('d',5,8)


