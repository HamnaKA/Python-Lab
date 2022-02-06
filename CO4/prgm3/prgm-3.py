class rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        self.a=self.l*self.b
    def __lt__(self, other):
        if(self.a < other.a):
            return "ob1 is lessthan ob2"
        else:
            return "ob2 is less than ob1"

i=int(input("enter the length of rectangle 1:"))
m=int(input("enter the breadth of rectangle 1:"))
x=int(input("enter the length of rectangle 2:"))
y=int(input("enter the breadth of rectangle 2:"))


r1=rectangle(i,m)
r1.area()
r2=rectangle(x,y)
r2.area()        
print(r1<r2)
