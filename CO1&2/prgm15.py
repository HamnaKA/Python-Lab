n=int(input("enter a number"))
a=0
s=0
while n>0:
    s=n%10
    a=a+s
    n=int(n/10)
print(a)
