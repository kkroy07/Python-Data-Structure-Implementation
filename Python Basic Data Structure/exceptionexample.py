x=int(input("Enter a number"))
y=int(input("Enter a number"))
try:
    z=int(x)/int(y)
except ZeroDivisionError as e:
    print('Division by Zero Exception',e)
    z = None
except Exception as e:
    print("Unknown exception",e)
print("Division is :",z)

