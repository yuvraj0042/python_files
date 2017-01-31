a=input("enter the number")
f=1
if a<0:
    print("factorial does not exist")
elif a==0:
    print("the factorial of 0 is 1")
else:
    for i in range(1,a+1):
      f=f*i
    print("the factorial of",a,"is",f)
