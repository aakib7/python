import random
age = int(input("Enter your Age: "))

if age >= 18:
    print("Your age is above 18:")
else:
    print("You are Under 18:")



if age == 100:
    pass # pass do nothing for empty if block
print("After Pass:")

# Excersise (Number Gussing)

winning_number = random.randint(1,100)
guessed_number = int(input("Enter a Guesswd Number: "))

if winning_number == guessed_number:
    print("You Won")

if guessed_number > winning_number:
    print("Ohhh!! You Lose try Again, your guess is to high")
    print(f"Actual number is: {winning_number}")

else:
    print("Ohhh!! You Lose try Again, your guess is to Low")
    print(f"Actual number is: {winning_number}")

# Solution 2

# else:
#     if guessed_number > winning_number:
#         print("Ohhh!! You Lose try Again, your guess is to high")
#         print(f"Actual number is: {winning_number}")
    
#     else:
#         print("Ohhh!! You Lose try Again, your guess is to Low")
#         print(f"Actual number is: {winning_number}")

# And or
 
name, age= input("Enter Your Name and age(,):").split(",")
age = int(age)
name = name.lower()

if age == 21 and name == "aaqib":
    print("and statement True:")
if age == 20 or name == 'aaqib javed':
    print("or Statement True:")
else:
    print("False Statements:")

# Excersise 2(Watch CoCo)

name, age= input("Enter Your Name and age(,):").split(",")
frist_character = name.strip()[0]
age = int(age)

if frist_character.lower() == "a" and age >10:
    print("You can Watch movie CoCo:")
else:
    print("Sorry you can't watch movie coco:")

age = int(input("Enter Your Age:"))

if 0 < age <= 3:
    print("Ticket Price: Free")
elif 4 <= age  <= 10:
     print("Ticket Price: 100")
elif 11 <= age  <= 60:
    print("Ticket Price: 200")
else:
    print("Ticket Price: 120")

name = "AAQIB"

if 'a' in name or 'A' in name:
    print(f"a present in:{name}")
else:
    print("Not Present:")

if 'z' in "zain":
    print("z is present:")
else:
    print("z not present:")

# check empty or not

name = ""
if name:
    print("not Enpty:")
else:
    print("Empty:")
x = 1;
if not x == 10: # if x !=10
    print("hello")

# While Loop:

x = 0
total = 0
while x <= 10: # Table
    answer = 2 * x
    print(f"2 * {x} = {answer}")
    x = x + 1

#    Sum of frist n number: ex

total_number = int(input("Enter the number till you want to add number:"))
while x <= total_number:
    total += x
    x += 1
print(total)

#    Sum of user number(123344): ex

number = input("Enter number consist of at least 2 digits:")
while x <= len(number)-1:
    total += int(number[x])
    x += 1
print(total)

# print charecter frequency in name(not repeating character in output): ex

name = input("Enter name:")
temp_variable = ""
while x < len(name):
    if name[x] not in temp_variable:
        temp_variable += name[x]
        print(f"{name[x]} : {name.count(name[x])}")
    x += 1

# For Loop:

for i in range(1,10):
    print(i)

# For Loop:(sum of 10)

for i in range(1,11):
    total += i
print(total)

# For Loop:(sum of digits)

number = input("Enter number consist of at least 2 digits:")
for i in range(len(number)):
    total += int(number[i])
print(total)

# print charecter frequency in name(not repeating character in output): ex

name = input("Enter name:")
temp_variable = ""
for i in range(len(name)):
    if name[i] not in temp_variable:
        temp_variable += name[x]
        print(f"{name[i]} : {name.count(name[i])}")

# Break 

for i in range(1,11):
    if i == 4:
        break
print(i)

# continues(print 1 to 10(not 5))

for i in range(1,11):
    if i == 5:
        continue
    print(i)

# Excersise (Number Gussing)

winning_number = 67
bool = True
total_try = 1
while bool:
    guessed_number = int(input("Enter a Guessed Number: "))
    if winning_number == guessed_number:
        print(f"You Won, in {total_try}:")
        bool = False
    else:
        if guessed_number > winning_number:
            print("Ohhh!! You Lose try Again, your guess is to high")            
        else:
            print("Ohhh!! You Lose try Again, your guess is to Low")           
    total_try += 1

# Step argument:

for i in range(0,11,2):
    print(i)

for i in range(10,0,-1):
    print(i)

# String for loop:
name = "aaqib"
for char in name:
    print(char)

num = "1234" # Sum of 1234
for numbers in num:
    total += int(numbers)
print(f"total:{total}")











 