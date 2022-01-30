"""swapping last two characters"""
s=input("enter the string:")
a=s[0]
b=s[1]
c=s[-1]
d=s[-2]
s=s[2:-2]
snew=s.replace(a,b)
snew1=s.replace(c,d)
print("the result is",c+d+snew1+b+a)
