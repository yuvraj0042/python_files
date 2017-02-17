def make_incrementor(n):
    return lambda x:x+n
f=make_incrementor (input("enter the value"))
print f(0)
print f(1)
print f(15)
