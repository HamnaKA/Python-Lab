import math
list1=[]
num=int(input("enter a range from 1000 to 9999:"))
if num>999:
   for i in range(1000,num):
       if i%2==0:
          root = math.sqrt(i)
          if int(root + 0.5) ** 2 ==i:
              list1.append(i)
   print(
   print(list1)
else:
    print("invalid entry")
          
