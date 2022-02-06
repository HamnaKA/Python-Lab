list1=input("enter the color list1")
list2=input("enter the color list2")
result=[]
c=list1.split()
d=list2.split()
for i in c:
    for j in d:
        if(i!=j):
            result.append(i)
print(result)

      
