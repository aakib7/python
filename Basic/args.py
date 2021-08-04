def addition(a,b):
    sum = a + b
    print(sum)

# addition(1,2)
# addition(1,2,3) # error 1

# solution of error 1
def addition(*args): # it take as many as argument as u want and create a tuble
    sum = 0
    for numbers in args:
        sum += numbers
    return sum

def mul(num,*args): # 1st argenrt not belong to tuple
    print(num)
    m = 1
    print(args)
    for i in args:
        m *= i
    return m

def mul1(num,n,*args): # 1st and 2nd argenrt not belong to tuple
    print(num)
    print(n)
    m = 1
    print(args)
    for i in args:
        m *= i
    return m

def average(*args):
    sum = 0
    for i in args:
        sum += i
    return sum/len(args) 

def excersice(num,*args):
    new_list = []
    power = 0
    if len(args) == 0:
        print("you did not pass args:")
        return -1
    else:
        for i in args:
            power = i ** num
            new_list.append(power)
        return new_list

def excersice1(num,*args): # excersise and this same
    if args:
        return [i**num for i in args]
    else:
        print("you didnot pass args:")





# print(addition(1,2,3,4))
# print(addition(1,2,3,4,4,5,6,7,8,65,4,3))
# print(mul(33,7,8)) # num = 33
# print(mul1(33,7,8,3)) # num =33 n=7

numbers = [1, 3, 5, 6]
## if we have list and we want to pass it to function we need to unpack list frist by using *
print(average(*numbers))

print(excersice(3,2,3,4))
print(excersice(3,*numbers))

# **kwargs

def info(**kwargs): # take arguments with keywords and return in dictionary form/ gether in dic form
    # print(kwargs)
    for key, value in kwargs.items():
        print(f"{key} : {value}")
d = {
    'name' : "aaqib",
    'age' : 21,
    'mail' : "ajmehdi123@gmail.com"
}

# info(name = "aaqib",age = 21,mail = "ajmehdi123@gmail.com")
info(**d)  # dictionary unpacking

# if use all 4 
def all_type_argunemts(name,*args, last_name = "javed",**kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

all_type_argunemts('aaqib', 12,23,32,45 ,a=1,b=2,c=4,d=9)


def ex2(*args):
    l = []
    for names in args:
        l.append(names.title())
    return l

def exe2(list_name,**kwargs): # dictionary contain reverse_name = True , kwargs is optionAL
    if kwargs.get('reverse_name') == True:
        return [name[::-1].title() for name in list_name]
    else:
        return [name.title() for name in list_name]

a = ["aaqib", "javed"]
print(exe2 (a,reverse_name = True))