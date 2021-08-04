import requests as rs
response =  rs.get("http://www.cuilahore.edu.pk")

# if response.status_code == 200:
if response:
    print("Request make Success!")
    # response.encoding = 'utf-8'
    # print(response.text)
    # print(response.json())
    # print(response.headers)
    print(response.headers['Content-Type'])
else:
    print("Not Found!")
# print()
# print(response.content) # or response.text 
# print()
# print(response.headers) 
# print()
# print(response.headers['Content-Type'])