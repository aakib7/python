
flag = True
total = 1
while flag:
    number = int(input("Enter Number:"))
    if number == -1:
        break
    total += number
    
print(total)
