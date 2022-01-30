test=input("enter the string:")
all= {}
for i in test:
    if i in all:
        all[i] += 1
    else:
        all[i] = 1
print ("The character frequency of string is:\n "+str(all))
