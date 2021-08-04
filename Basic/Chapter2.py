# Concatination
frist_name = "Aaqib"
last_name = "Javed"
print(frist_name +" "+ last_name)
#print("Aaqib" + 3) error
print("Aaqib" + "3")
print("Aaqib" + str(3))
print(frist_name * 3)

#Input
name = input("Enter your name:")
print("Enter your University Name:")
university_name = input()
print("Hello "+name+"your University name is:"+university_name)

#Integer
number1 = int(input("Enter 1 Number:"))
number2 = int(input("Enter 2 Number:"))
total = number1 + number2
print("sum of two number is:"+str(total))
marks = float(input("Enter The Marks of English subject:"))
print("your Marks:"+str(marks))
x = marks + total
print(x)

#Decleration
name, age = "aaqib", 21
print(name)
print(age)
x = y = z = 5
print(x + y + z)

#Two Inputs

name,age=input("Enter your name and age: ").split() #Type name and give space and then type age
print(name)
print(age)

name,age=input("Enter your name and age: ").split(",") #Type name and , then type age

# #Formating

print("Hello {}, your age is {}".format(name,age))
print(f"Hello {name}, your age is {age}")
print(f"Hello {name}, your age is {int(age) + 3}")

#Excersise
num1,num2,num3=input("Enter 3 number for Average: ").split(",")
sum = float(num1) + float(num2) + float(num3)
average = sum / 3
print(f"Average of {num1}, {num2}, and {num3} is = {round(average,3)}")

#Indexes Of String

name = "Rayan"
# print(name[0] + "\n" + name[-1])
print(name[0:3]) #print Ray we give last (argument+1) 
print(name[-3:5])
print(name[:]) # whole String
print(name[1:]) # start from 1 to whole String
print(name[:4]) # start from 0 to 4 index

# Excersise (Reverse String)
name = input("Enter your Name:")
print(f" Your name in reverse order:{name[-1::-1]}")