num=int(input("enter the total number:"))
list=[]
for i in range(num):
    c=int(input("enter the number:"))
    if c>100:
        c="over"
    list.append(c)
print(list)
