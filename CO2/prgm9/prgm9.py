row=int(input("enter the rows:"))
for i in range(0,row+1):
    for j in range(i):
        print('*',end='')
    print("\n")
for i in range(row-1,0,-1):
    for j in range(i):
        print("*",end='')
    print("\n")
    
