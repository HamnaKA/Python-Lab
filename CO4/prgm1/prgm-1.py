class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        
    def area(self):
        self.a=self.length*self.breadth
        print("Area is :",self.a)
        return self.a
    def perimeter(self):
        self.p=2*(self.length+self.breadth)
        print("Perimeter is:",self.p)
i=int(input("enter the length of rectangle 1:"))
m=int(input("enter the breadth of rectangle 1:"))
x=int(input("enter the length of rectangle 2:"))
y=int(input("enter the breadth of rectangle 2:"))


r1=rectangle(i,m)
e=r1.area()
r1.perimeter()

r2=rectangle(x,y)
x=r2.area()
r2.perimeter()
        
if e>x:
    print("area of rectangle 1 is great")
elif e<x:
    print("area of rectangle 2 is great")
else :
     print("both area are same")
