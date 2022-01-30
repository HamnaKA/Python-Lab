class time:
    def __init__(self,hour,minute,second):
        self.__hour=hour
        self.__minute=minute
        self.__second=second
      
    def __add__(self,other):
       second=self.__second+other.__second
       minute=self.__minute+other.__minute+(second/60)
       hour=int(self.__hour+other.__hour+(minute/60))
       minute=int(minute%60)
       second=int(second%60)
       print("The sum of Time\t:")
       return str(hour)+"hours\t"+str(minute)+"minutes\t"+str(second)+"seconds"
print("Enter the Time 1")
h1=int(input("Enter the Hour:"))
m1=int(input("Enter the Minute:"))
s1=int(input("Enter the Second:"))
print("Enter the Time 2")
h2=int(input("Enter the Hour:"))
m2=int(input("Enter the Minute:"))
s2=int(input("Enter the Second:"))


y=time(h1,m1,s1)
z=time(h2,m2,s2)
print(y+z)

