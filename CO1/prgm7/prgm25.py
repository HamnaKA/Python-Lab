list1=int(input("enter the total numbers in list1:"))
list2=int(input("enter the total numbers in list2:"))
a=[]
b=[]
for i in range(list1):
        one=int(input("enter the number in list1"))
        a.append(one)
for i in range(list2):
        two=int(input("enter the number in list2"))
        b.append(two)
if len(a)==len(b):
        print("two lists are same length",len(a),len(b))
else:
        print("two lists are not same length",len(a),len(b))
result1 = all(element == a[0] for element in a)
result2 = all(element == b[0] for element in b)
if (result1==result2):
   print("list are Equal")
else:
   print("list are not equal")
common=0
for i in a:
           if i in b:
                    common=1
if(common==0):
      print("The lists have no common elements")
else:
      print("The lists have common elements")
                    
