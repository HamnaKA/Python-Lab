str=input("enter the line of text:")
str=str.split()
i=0
count=0
while i<len(str):
    count=0
    for j in str:
        if str[i]==j:
            count=count+1
    print(str[i],"present",count)
    i=i+1
