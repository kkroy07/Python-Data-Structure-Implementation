import json
with open("D://jsondata//book.txt","r") as f:
    s = f.read()
print(s)
print(type(s))
book=json.loads(s)
print(book)
print(type(book))
print(book['tom']['address'])
for person in book:
    print(book[person])
