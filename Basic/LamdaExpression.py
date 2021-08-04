# def add(a,b):
#     return a+b
## Lambda

# add = lambda a,b : a + b
# a = lambda a,b : a * b
# is_even = lambda a: a % 2 == 0
# last_char = lambda name: name[-1]
# fun = lambda str : print("true") if len(str) > 5 else print("false")
# print(add(1,9))
# print(a(1,9))
# print(is_even(7))
# print(last_char("aaqib"))
# fun("aaqib javed")

## Enumerate 
## use enumerate fun. w for loop to track position of a item in list/tupe

## without Enumerate
name = ["aaqib", "javed", "mehdi"]
# pos = 0

# for names in name:
#     print(f"{pos} ---> {names}")
#     pos += 1

## without Enumerate
# for pos, names in enumerate(name): # in enumerate we put list/ tuple name 
#     print(f"{pos} --> {names}")

# def find_index(list_name,n):
#     for pos ,name in enumerate(list_name):
#         if n == name:
#             return pos
#     return -1

# print(find_index(name,"javed"))

##Map()
numbers = [1,2,3,4,5,6,7,8]
# def square(n):
#     return n**2

# a = [square(1),square(2),square(3)]  ## and so on // so use map()
# b = map(square,numbers)
# print(a)
# print(list(b))
# ## using lambda
# c = map(lambda a: a**2,numbers) ## function is defines here 
# print(list(c))
# ## using list comp.
# d = [i**2 for i in numbers]
# print(d)

# def myfunc(a, b):
#   return a + b

# x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))

# print(x)

# #convert the map into a list, for readability:
# print(list(x))

## filter()

# def is_even(a):
#     return a%2 == 0

# even = tuple(filter(is_even,numbers))
# odd = tuple(filter(lambda a: a%2 != 0,numbers))
# even1 = list(filter(is_even,numbers))
# even2 = list(map(is_even,numbers))
# print(even)
# print(even1)
# print(even2)
# print(odd)

# ## ietrable only one time(filter and map)
# even_inFilter = filter(is_even,numbers) 
# for i in even_inFilter:
#     print(i)
    
## Zip 
# user_id = [1, 2, 4, 5]
# user_name = ["aaqib", "javed", "mehdi", "ali"]
# users = list(zip(user_id,user_name))
# print(users)

# user_id1 = [1, 2]  ## (if one list is shorter new touble is that length)
# user_name1 = ["aaqib", "javed", "mehdi", "ali"]
# users1 = list(zip(user_id1,user_name1))
# print(users1)
# ## list to dictioary
# a = dict(users1)
# print(a)

# user_id1 = [1, 2]  ## (more than 2 list)
# user_name1 = ["aaqib", "javed", "mehdi", "ali"]
# user_adress = ["lahore","karachi"]
# users1 = list(zip(user_id1,user_name1,user_adress))
# print(users1)

# * operator with list
# l = [(1,2), (3,4), (5,6)]
# l1 = list(zip(*l))
# print(l1)

# ll = [(1,2), (3,4), (5,6), (7,8)]  ## as l1=(1,3,5,7) l2= (2,4,6,8)
# ll1,ll2 = list(zip(*ll))
# print(ll1)
# print(ll2)

## Ex
# def list_average(l1,l2):
#     average = []
#     for pair in zip(l1,l2) :
#         a = sum(pair)/len(pair)
#         average.append(a)
#     print(average)

# list_average([1,2,3],[4,5,6])

# def list_average(*args): ## args take list and covert into tuple as([1,2]......)
#     average = []
#     for pair in zip(*args) :  ## * b/c unpacking of tuple
#         a = sum(pair)/len(pair)
#         average.append(round(a,2))
#     print(average)

# aa = lambda * args :[round(sum(pair)/len(pair),4) for pair in zip(*args)] ## list com. and lambda
# list_average([1,2,3],[4,5,6],[4,6,7])
# print(aa([1,2,3],[4,5,6],[4,6,7]))

## all(give true if all value has true in list)
## any(give true if one value has true in list)
# num1 = [2, 4, 6, 5]
# print(all([n % 2 == 0 for n in num1]))
# print(any([n % 2 == 0 for n in num1]))

# def practice(*args): # if some one give input a string
#     if all([(type(arg) == int or type(arg) == float) for arg in args]):
#         total = 0
#         for num in args:
#             total += num
#         print(total)
#     else:
#         print("Enter onlt int of floting value:")
# practice(1,2,3,4,5,6,6,'111')

### sorted()
bike = [
    {"model":125, 'price':1000},
    {"model":150, 'price':12000},
    {"model":200, 'price':15000},
    {"model":70, 'price':100}
]

## dictionary with respect to price
print(sorted(bike, key = lambda d: d.get("price"))) ## min to max
print(sorted(bike, key = lambda d: d.get("price"),reverse = True)) ## max to min


