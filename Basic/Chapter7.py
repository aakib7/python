# dictionary creation
user = {"name" : "Aaqib", "age" : 24, "Id" : "sp19-bse-087"}
user1 = dict(name = "aaqib", age = 21, id = "sp19-087")
print(user)
print(user1)

# Access data from dictionary
print(user["name"])
print(user["age"])
print(user["Id"])

print(user1["name"])
print(user1["age"])
print(user1["id"])

# dictionary with List
user_info = {
    'name' : 'aaqib',
    "age" : 24,
    "fav_movies" : ["coco", "titanic",],
    "fav_seasons" : ["Friends", "OutLanders"],
    "marks" : [88, 85, 80, 75]
}
print(user_info)

# Check key present or not #(only key check)
if "name" in user_info:
    print("present")
else:
    print("not present")

# Check values present or not (only values check)
if "aaqib" in user_info.values():
    print("present")
else:
    print("not present")

# Looping
for i in user_info: # print keys
    print(i)

for i in user_info.values(): # print values
    print(i)

user_info_keys = user_info.keys() # store keys in this variable
print(type(user_info_keys))
print(user_info_keys)

user_info_items = user_info.items() # return [('name','aaqib'),(),()]
print(type(user_info_items))
print(user_info_items)

for key, value in user_info.items():
    print(f"user info key is {key} and value is {value}")


for i in user_info["marks"]: # access perticular list
    print(i, end = " ")

print()

for i in user_info["fav_movies"]: # access perticular list
    print(i, end = " ")

# Add data
user_new = {}
user_new['name'] = "Ali"
print(type(user_new))
print(user_new)
user_info["cgpa"] = [3.35]
print(user_info)

# delete
user_info.pop("marks")
print(user_info)

# # update
user_more_info = {
    'name' : "aaqib javed", 
    'hobbies' : ["codding"]
}
user_info.update(user_more_info)
print(user_info)

 # methods
d = dict.fromkeys(['name','age'], 'unknown')
print(d)
d = dict.fromkeys(['name','age'],['unknown','unknown'])
print(d) 
d1 = d.copy()
print(d1)

print(d.get('names')) # names not in dictionary so it is error without get now its value is none
print(d.get('names', "not present")) # none override
di = {
    'age' : 12,
    'age' : 13
} 
# if two same keys 1st is replaced with 2nd 
print(di)

## Excerse 
def cube_finder(number):
    cube = {}
    value = 0
    for i in range(1,number+1):
        value = i * i * i
        cube[f"{i}"] = value # cube[i] = value
    return cube
print(cube_finder(10))

def word_counter(string):
    count = {}
    for char in string:
        count[char] = string.count(char)
    return count
print(word_counter("aaqib javed"))

name = input("Enter Your Name:")
age = int(input("Enter Your Age:"))
fav_movie= input("Enter your fovourit movie name seprate by comma:").split(",")
fav_season= input("Enter your fovourit  season name seprate by comma:").split(",")

user_input = {
    'name' : name,
    'age' : age,
    'fav_movie' : fav_movie,  # as seprate by comma so atomatically became a list
    'fav_season' : fav_season
}

for key, value in user_input.items():
    print(f"{key}: {value}")