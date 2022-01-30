str1=input("enter the string:")
if str1[-3:] == 'ing':
      str1 += 'ly'
else:
      str1 += 'ing'
print(str1)
