"""removing a character"""
print("enter the name:")
s=input()
n=int(input("enter the position of character to be removed:"))
a=s[0:n-1]
b=s[n:]
print("the new string is",a+b)