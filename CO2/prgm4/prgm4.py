import math
list1=[]
num=int(input("enter the range1:"))
num2=int(input("enter the range2:"))

if num>999 and num2<10000:
   for i in range(num,num2+1):
       for j in str(i):
          if (int(j)%2!=0):
              break
       else:
          root = math.sqrt(i)
          if(root%1==0):
             list1.append(i)
         
   print(list1)
else:
    print("Invalid entry")

          
