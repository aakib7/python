#Prime Number Check:
# num = int(input("Enter a number: "))  
# if num >1:
#     for i in range(2,num):
#         if (num % i ) == 0:
#             print("Number is not prime:")
#             print(f"{i}, time {num//i} is {num}:")
#             break;
#     else:
#         print("Number is Prime:")

# else:
#     ptint("Not Prime:")

# Factorial: fac of 4! is 24

# number = int(input("Enter a Number for Fsctorial:"))
# factorial = 1
# if number > 1:
#     for i in range(1,number+1):
#         factorial *= i
#     print(f"Factorial of {number}! is = {factorial}")
# else:
#     if number == 1 or number ==0:
#         print("Factorial is: 1")
#     else:
#         print("Enter a +ve Integer:")

foo = 56
print (format(foo, '.1f'))
print (format(foo, '.2f'))
print (format(foo, '.3f'))
print (format(foo, '.5f'))


def avg(a,b=0.0,c=0.0):
    average = 0.0
    if b == 0:
        average = a
        return round(average,2)
    elif c==0:
        sum = a + b 
        average = sum / 2
        return round(average,2)
    else:
        sum = a + b + c
        average = sum / 3
        return round(average,2)
    
avg(7) 
avg(2,5)