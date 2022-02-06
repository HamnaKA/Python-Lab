"""first and last character exchanged"""
c=input("enter the string:")
a=c[0]
b=c[-1]
c=c[1:-1]
cnew=c.replace(a,b)
print("the new string is:",b+cnew+a)
