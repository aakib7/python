class Human:
    def __init__(self):
        self.name = "AAKIB CHAUDHRY"
        self.age = 21
    
    def compare(self,other):
        return self.age == other.age
    
    
human1 = Human()
human2 = Human()

print(human1.name)
print(human2.name)
human2.name = "ALI"
print(human2.name)
print(human1.compare(human2)) # Here human1 is self and Human2 is otther
print(human2.compare(human1)) # vise varsa
human2.age = 23
print(human2.compare(human1))