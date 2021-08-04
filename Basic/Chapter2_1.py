name = "Aaqib Javed mehdi"

print(len(name)) # count with spacing(leng())
print(name.lower()) # all character is Lower
print(name.upper())  # all character is Upper
print(name.title())  # frist character is Upper and remaining is lower
print(name.count("a")) # count a character in a string (case sensitive)
print(name.lower().count("a")) 

print(name.strip()) # Remove starting and end space 
print(name.lstrip()) # Remove only starting/left spacing
print(name.rstrip()) # Remove ending/right spacing

print(name.split(" ")) # Returns a list where the text between the specified separator becomes the list items.

print(name.replace("A","a")) # Replace a character in a String
print(name.replace(" ","")) # Remove all the spaces in a string
string = "ali is a good boy, he is 20 year old"
print(string.replace("is","was")) # Replace all 
print(string.replace("is","was",1)) # Replace only frist is with was 
print(string.replace("is","was",2)) # Replace only frist two is with was 

print(string.find("is")) # Return the Starting index of is
is_position1 = string.find("is")
print(string.find("is",is_position1+1)) # find after frist is  (so on..)

name = "Aaqib" # give 7 spaces on both sides of name
print(name.center(len(name)+14," "))
print(name.center(len(name)+8,"*"))  # add 4 * on both sides of name

name = "aaq"
name = name + "ib" # or name += "ib"
print(name)
age = 23
print(age)
age += 7 # age = age + 7
print(f"After + = {age}")
age -= 3 # age = age -3
print(f"After - = {age}")
age *= 2
print(f"After * = {age}")

# Excersise 

name,charcter = input("Enter name and character you want to count:").split(",")
print(f"length of name:{len(name)}")
print(f"Count of Characer:{charcter}in{name} is={name.strip().lower().count(charcter.strip().lower())}")
