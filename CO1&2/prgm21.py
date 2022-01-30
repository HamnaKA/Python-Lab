y1=int(input("enter the current year:"))
y2=int(input("enter the future year:"))
for i in range(y1,y2):
   if(i%4==0) and (i%100!=0) or (i%400==0):
      print(i)
