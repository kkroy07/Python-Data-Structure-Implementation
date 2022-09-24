book={}
book['tom']={
    'name':'tom',
    'address':'1 red street, NY',
    'phone':9890855905
}
book['bob']={
    'name':'bob',
    'address':'1 green street, NY',
    'phone':7001398133
}
import json
s=json.dumps(book)
print(s)
with open("D://jsondata//book.txt","w") as f:
    f.write(s)

