nums=[1,2,3,4,5,6,7,8]
even=[]
for i in nums:
    if i % 2 ==0:
        even.append(i)
print(even)
#List comprehension
evenl=[i for i in nums if i % 2 ==0]
print(evenl)
sqr=[i*i for i in nums]
print(sqr)