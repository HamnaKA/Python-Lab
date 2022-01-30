def amstrong(n):
 res=0
 org=n
 while org > 0:
        r=org%10
        res=res+r ** 3
        org=org//10
 if n == res:
  print("amstrong")
 else:
  print("not amstrong")
n=int(input("enter the number:"))
amstrong(n)


