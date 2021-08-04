cubes = [numbers ** 3 for numbers in range(1,10)]
print(cubes)
negative_numbers = [-(number) for number in range(1,11)]
print(negative_numbers)

names = ["aaqib", "javed", "mehdi"]
# #store last character of every name in new list:
last_character = [name[-1] for name in names]
print(last_character)

# Ex revese strind method

def reverse_string(l):
    return [reverse[::-1] for reverse in l]

print(reverse_string(names))

# Seperate even odd from a list: if/else
l = list(range(1,21))
print(l)
even_numbers = [number for number in l if number % 2 == 0] 
odd_numbers = [number for number in l if number % 2 != 0] 
print(even_numbers)
print(odd_numbers)

# ex seperate integers and float:
def number_to_string(l):
    return [f"{i}" for i in list_mix if type(i) == int or type(i) == float] # [str(i)......]
list_mix = [True, "ali", [1,2,3], 1, 2.87, 6]

print(number_to_string(list_mix))

# if elen nb put - else *2 (if/else)
mix = [-i if i%2 !=0 else i*2 for i in range(1,16)]
print(mix)

# Nested 

l = [[i for i in range(1,4)] for j in range(3)]
print(l)
l = [[i for i in range(1,4)], [i for i in range(4,7)], [i for i in range(8,11)]]
print(l)
