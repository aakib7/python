s = {1,2,3,3}
print(s) # remove duplicate
s1 = set(range(15))
print(s1)

# remove duplicate from list 
l = [1,2,4,6,2,6]
s3 = set(l)
print(s3)
# remove duplicate from list and store in other list
l = list(set(l))
print(l)

# Methods
s.add(10)
s.remove(1)
s.discard(3) # remove 3 if exist if not exist no error
s4 = s.copy()
print(s)
print(s4)
s.clear()
print(s)
mix = {1,2.9,"aaqib"}
print(mix)

if "aaqib" in mix:
    print("Present")
else:
    print("Not Present:")

for i in mix:
    print(i)

a = s | mix
b = s & mix
print(a)
print(b)