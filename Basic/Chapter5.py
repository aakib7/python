# List is Created by put [] 
 
numbers = [1, 2, 3, 4]
words = ["aaqib", "Javed", "Mehdi"]
mixture = [1, 2, 3, "Ali", 2.3, "Hamza", None]

print(numbers)
print(words)
print(mixture)

print(numbers[2]) by index

for num in numbers:    # Print as  1 2 3 4 not as  ([1,2,3,4]) single number (Whole List)
    print(num , end =' ') 

# print frist 3 element of list:

for i in range(3):  # (0,1,2)
    print(numbers[i])

i = 0
while i < len(words):
    print(words[i])
    i += 1

# Change in List:

mixture[0] = 'One'
print(mixture)
mixture[1:] = ["two", "Three"]  # All other (Above that index element gone)
print(mixture)
words.append("aaaa")
print(words)

# add data
fruit1 = []
fruit1.append("mango")
fruit1.append("graps")
fruit2 = ["Orange", "Apple"]
t = fruit1 + fruit2
print(t)
fruit1.append(fruit2) # Store list inside other list
print(fruit1)

# Delete data

fruits = ["apple", "oranges", "banana", "mango", "apple"]
fruits.pop() # remove last
print(fruits)
fruits.pop(1) # remove 1 index element
print(fruits)
del fruits[1] # remove 1 index element
print(fruits)
fruits.remove("banana") # if two exist with same name it delete 1 
print(fruits)

if "apple" in fruits:
    print("present:")
else:
    print("Not Present:")

# Other Methods:

print(fruits.count("apple"))
fruits.sort() # sort list permanently 
print(sorted(fruits)) # only for sorted printed purpose
fruits.clear() # clear all the list
f = fruits.copy()
print(f)

fruits_name = ["apple", "oranges", "banana", "mango"]
print(fruits == fruits_name) # false b/c dont have same values
print(fruits is fruits_name) # false b/c dont have same location(object)

# Split and join 

name = "aaqib javed mehdi".split()
print(name)
name = "aaqib, javed, mehdi".split(",")
print(name)
print(",".join(fruits_name))


number_range = list(range(1,11))
print(number_range)

nb = number_range.pop()
print(nb)

print(number_range.index(9))

def negitive_list(l): # negative a list using new list
    new_list = []
    for i in l:
        new_list.append(-i)
    return new_list

def negitive_list(l): # negative a list using same list
    count = 0
    for i in l:
        l[count] = -i 
        count += 1
    return l 

print(negitive_list(number_range))

def squre_list(l): # Squre of list
    count = 0
    for i in l:
        l[count] = i * i 
        count += 1
    return l 

def reverse_list(l):
    return l.reverse()

def reverse_list1(l):  
    return l[::-1]

def reverse_list2(l):  
    new_list = []
    for i in range(1,len(l)+1):
        poped_item = l.pop()
        new_list.append(poped_item)
    return new_list

def reverse_list_words(l):
    new_list = []
    for i in range(len(l)):
        a = l.pop()
        new_list.append(a[::-1]) 
    return reverse_list(new_list)

def reverse_list_words1(l):
    new_list = []
    for i in l:
        new_list.append(i[::-1]) 
    return new_list

def filter_even_odd(l):
    odd = []
    even = []
    for i in l:
        if (i % 2) != 0 :
            odd.append(i)
        else:
            even.append(i)
    output = [odd, even]
    return output

def common_elements(a,b):
    output = []
    for i in a:
        e = i 
        for j in b:
            if (j == e):
                if e not in output:
                    output.append(e) # prevent dublication
    return output

def common_elements1(a,b):
    output = []
    for i in a:
        if i in b:
            output.append(i)
    return output

def sublist_counter(l):
    count = 0
    for i in l:
        if type(i) == list:
            count += 1
    return count

x = [1, 5, 7, 4, 5, 100, 31] 
y = [1, 5, 7, 4, 5, 100, 31, [1,2,3]]
b = ["aaqib", "javed", "mehdi"]
print(squre_list(number_range))
print(reverse_list2(a))
print(reverse_list_words1(b),"u")
print(filter_even_odd(number_range))
print(common_elements(number_range,x))
print(common_elements1(number_range,x))
print(min(number_range))
print(max(number_range))
print(sublist_counter(y))