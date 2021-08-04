cube = {num:num**3 for num in range(1,11)}
square = {f"square of {num} is" : num**2 for num in range(1,11)}
# print(cube)
# # print(square)

# for k,v in square.items():
#     print(f"{k} = {v}")

name = "aaqib"
word_count = {char:name.count(char) for char in name}
print(word_count)

odd_even = {i:('even' if (i % 2)==0 else 'odd') for i in range(1,10)}
print(odd_even1)


