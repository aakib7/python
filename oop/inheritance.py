# Single level inheritance
# class A:
    
#     def __init__(self):
#         print("in A init")
    
#     def f1(self):
#         print("feature 1")
    
#     def f2(self):
#         print("feature 2")

# class B(A):
    
#     def __init__(self):
#         print("in B init")
#         super().__init__() # class super class init
    
#     def f3(self):
#         print("feature 3")
    
#     def f4(self):
#         print("feature 4")
        
# b1 = B()
# b1.f2()


## MultiLevel 

class A:
    
    def __init__(self):
        print("in A init")
    
    def f1(self):
        print("Class A Here")
class B:
    
    def __init__(self):
        print("in B init")
            
    def f1(self):
        print("Class B here")
    
class C(A,B):
     
    def __init__(self):
        print("in C init")
        super().__init__()
        super().f1()
    
    def f1(self):
        print("jj")
        
c1 = C()
c1.f1()