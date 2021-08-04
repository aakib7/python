# def square(a):
#     return a * a

# s = square
# print(square(2))
# print(s(2))
# print(s.__name__) ## name of function

# l = [1,2,3,4,5,6]
# print(list(map(s,l)))

## function in argemrnt of other function
# def my_map(func,l):
#     new_list = []
#     for item in l:
#         new_list.append(func(item))
#     return new_list
# print(list(my_map(s,l)))

## function return function(closure/frist class function)
# def outer_fun():
#     print("outer")
#     def inner_fun():
#         print("inner")
#     return inner_fun

# var = outer_fun()  ## in var inner function return 
# var()  

# def outer(message):
#     def inner():
#         print(f"message is:{message}")
#     return inner

# var1 = outer("hello aaqib")
# var1()

def to_power(x):
    def to_calulate(n):
        return n ** x
    return to_calulate

cube = to_power(3)
print(cube(3))

squre = to_power(2)
print(squre(5))

power_five = to_power(5)
print(power_five(5))
