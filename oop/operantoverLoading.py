class Student:
    
    def __init__(self,m1,m2):
        self.mark1 = m1
        self.mark2 = m2
        
    def info(self):
        print(self.mark1 , self.mark2)
        
    def __add__(self,other):
        m1 = self.mark1 + other.mark1
        m2 = self.mark2 + other.mark2
        return Student(m1,m2)
    
    def __gt__(self, other):
        r1 = self.mark1 + self.mark2
        r2 = other.mark1 + other.mark2
        return r1 > r2
    def __str__(self):
        return f'{self.mark1} {self.mark2}'



s1 = Student(150,45)
s2 = Student(60,55)


# print(s1 + s2) # error but they belong to samr class as 2 Integers
s = s1 + s2
print(s.mark1)
print(s.mark2)
print(s1.mark1)

print(s1 > s2)
print(s1)

