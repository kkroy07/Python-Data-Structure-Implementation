f=open("D://jsondata//funny.txt","a")
f.write("\nI love kubernetes")
f.close()
f=open("D://jsondata//funny.txt","r")
s=f.read()
print(s)
for line in s:
    print(line)
    wc=line.split(' ')
    print(wc)
    print(len(wc))
f.close()