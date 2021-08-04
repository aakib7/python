matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(matrix[0]) # print [1,2,3]
print(matrix[0][1]) # print 2

# for i in matrix: # print [1,2,3]\n[3,4,5]\n[6,7,8]
#     print(i)
count = 0

for sublist in matrix: # frist time loop exicute [1,2,3] store in sublist and so on 
    count +=1
    print(f"{count} Sublist:")
    for i in sublist: # after 1st for loop 2nd loop exicute till (elements in sublist) 
        print(i)
            