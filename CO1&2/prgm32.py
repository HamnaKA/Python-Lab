n=int(input("enter the rows:"))
for i in range(n):
    for j in range(i+1):
        print('*',end='')
        print()
for i in range(n):
    for j in range(i,n):
        print("*",end='')
        print()
    
