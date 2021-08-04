example = ("one", "two", "three")
mixted = (1, 2, 3, "four", 6.09)
one_element_tuple = (1,)

# Methods
print(example)
print(example[0])
print(example.count("one"))
print(len(example))
print(example.index("one"))

# Loop
for i in mixted:
    print(i)

# One Element
print(one_element_tuple)
print(type(one_element_tuple))
for i in one_element_tuple:
    print(i)

# without prenthises
without_orenthises = "aaqib", "jAVED"
print(without_orenthises)
print(type(without_orenthises))

# Unpacking of touples
full_name = ("Aaqib", "Javed", "Mehdi") 
frist_name, midle_name, last_name = (full_name) # if valuue or variale > varible or vaule (Error)
print(frist_name)
print(midle_name)
print(last_name)

# List inside touple
list_inside_touple = (1,[123, 245, 545])
print(list_inside_touple)
list_inside_touple[1].pop()
print(list_inside_touple)
list_inside_touple[1].append("ali")
print(list_inside_touple)

num = (1,2,34,5,8,6)
print(max(num))
print(min(num))
print(sum(num))


def three_values(a,b,c):
    sum1 = a + b
    mul = a * b * c
    div = a // b
    return sum1, mul, div

print(three_values(3,2,3)) # return touple
addition, multiplication, division = three_values(15, 5, 3)
print(addition)
print(multiplication)
print(division)

# conversion
a = tuple(range(1,11))
print(a)
b = list((1,2,3,4,5,6))
print(type(b),"Elements:",b) # into list
c = str(("aqib", "javed"))
print(type(c),"Elements:",c) # t into String

