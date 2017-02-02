import math
print ("enter the value of factorise")
a=input("enter first digit")
b=input("enter second digit")
c=input("enter third digit")
x1=(-(b)+math.sqrt(b*b-4*a*c))/(2*a)
x2=(-(b)-math.sqrt(b*b-4*a*c))/(2*a)
print "the value of positivce x",x1, "the value of negative x",x2
