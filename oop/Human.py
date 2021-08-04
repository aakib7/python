class Human:
    def __init__(self,n,occup,sal):
        self.name = n
        self.occupation = occup
        self.salary = sal
        
    def do_work(self):
        if self.occupation.lower() == 'actor':
            print(self.name+" Is an Film Star, He is a great Actor.")
            print("He Charge "+str(self.salary)+" for a Film.")
        elif self.occupation.lower() == 'cricketer':
            print(self.name+" Is A Cricket Player, He is a Fantastic Player.")
            print("He Charge "+str(self.salary)+" for a Match.")

    def speak(self):
        print(self.name + " Who is a "+self.occupation+". Say Hello to You.")
    
tom = Human("Tom","Actor","$1M")
a = Human("Shahid Afridi","cricketer","$0.2M")
# print(tom.occupation)
tom.do_work()
tom.speak()
print()
a.do_work()
a.speak()
