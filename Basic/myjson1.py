import json as js

book = {}

book['Ali'] = {
    'name' : 'ali',
    'address' : '1 iqbal town Lahore',
    'phone' : '0301000002',
    'dob' : '19-2-2000'
}

book['hassan'] = {
    'name' : 'hassan',
    'address' : '1221 iqbal town Lahore',
    'phone' : '03010232002',
    'dob' : '19-2-20034'
}

s = js.dumps(book)
# print(s)
book = js.loads(s)
print(book)
print(book['Ali'])
print(book['hassan'])
print(book['hassan']['phone'])

for persons in book:
    print(book[persons])
