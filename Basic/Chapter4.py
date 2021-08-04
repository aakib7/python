def add(a,b):
    return a + b

def subtraction(a,b):
    total = a - b
    print(total)

def last_char(string):
    return string[-1]

def midle_char(string):
    return string[len(string)//2]

def odd_even(number):
    if number % 2 == 0:
        return f"The Number {number} is Even:"
    return "Odd Number:"

# def greater_number(a,b):
#     if a > b:
#         print(f"{a} is Greater then {b}")
#     else:
#         print(f"{b} greater then {a}")

def greater_number(a,b):
    if a > b:
        return a
    return b

# Nested Function:
def greatest(a,c,n):
    bigger = greater_number(a,c)
    return greater_number(bigger,n)

def is_palidrome(string):
    temp = string[-1::-1]
    if temp.lower() == string.lower():
        return True
    return False

def is_palidrome1(string):
    return string == string[::-1]

def fibonacci_series(n):
    frist_number = 0
    second_number = 1
    if n == 1:
        print(frist_number)
    elif n == 2:
        print(frist_number, second_number)
    else:
        print(frist_number, second_number, end=" ")
        for i in range(n-2):
            frist_number = second_number
            next_number = frist_number + second_number
            second_number = next_number
            print(second_number, end = " ")
    print()

def user_info(name,gender,age=23):
    print(f"name:{name} gender:{gender},age:{age}")

def user_info1(name,gender = 'Male',age=25):
    print(f"name:{name} gender:{gender},age:{age}")
          
# print(add(1,2))
# print("aaqib","Javed")
# subtraction(10,5)

# print(last_char("aaqib"))
# print(midle_char("AAIB"))
# print(odd_even(21))

# num1 = int(input("Enter Number 1:"))
# num2 = int(input("Enter Number 2:"))
# num3 = int(input("Enter Number 3:"))

# print(greatest(num1,num2,num3))

# print(is_palidrome("madam"))
# print(is_palidrome("aaqib"))
# print(is_palidrome1("nan"))
# print(is_palidrome1("nanm"))

#fibonacci_series(10)
# user_info("aaqib","male")
# user_info("aaqib","male",20)  # OverRide defalut value

# user_info1("aaqib")
# user_info1("aaqib","M",18)

x = 5 # Global Variable 

def val():
    x=10  # Change not effect global variable 
    print(x)
def val2():
    print(x)
def val3():
    global x  # Change  effect global variable 
    x = 19
    print(x)

val()
val2()
val3()
print(x)