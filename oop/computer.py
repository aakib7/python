class Computer:
    
    def __init__(self,c,r):
        self.cpu = c
        self.ram = r
    
    def config(self):
        print("Configration is:",self.cpu," ", self.ram)
        
com1 = Computer('i5','16gb')
com2 = Computer('i7','32gb')
com1.config()
# com2.config()
Computer.config(com2)
