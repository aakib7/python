# with open("funny.txt",'w') as f:
#     f.write("This way, we are guaranteeing that the file is properly closed even if an exception is raised that causes program flow to stop.")

f = open('funny.txt','r')
new_file = open('funny2.txt','w')
# f.write("\nHello i'm Aakib ")
# f.close()
# fs = open('funny.txt','r')

# print(fs.read())
# fs.close()
text = ''
total = 0
for lines in f: 
   text += lines
   tokens = lines.split(' ')
   total +=len(tokens)
  

print(text)
new_file.write(text +'\n Words in thos file = '+str(total))


f.close()
new_file.close()