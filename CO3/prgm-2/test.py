import graphics
from graphics import circle,rectangle
from graphics.dgraphics import cuboid,sphere
from graphics.circle import *

x=int(input("enter the radius of circle:"))
c=circle.circle_area(x)
d=circle.circle_peri(x)
print("Area of a circle is",c)
print("Permeter of a circle is",d)

a=int(input("enter the length of rectangle:"))
b=int(input("enter the height of rectangle:"))
s=rectangle.rect_area(a,b)
t=rectangle.rect_peri(a,b)
print("Area of a rectangle is ",s)
print("Permeter of a rectangle is",t)

v=int(input("enter the length of cuboid:"))
w=int(input("enter the height of cuboid:"))
m=int(input("enter the breadth of cuboid:"))
z=cuboid.cuboid_area(v,w,m)
q=cuboid.cuboid_peri(v,w,m)
print("Area of a cuboid is",z)
print("Permeter of cuboid is",q)


ss=int(input("enter the radius of sphere:"))
h=sphere.sphere_area(ss)
tt=sphere.sphere_peri(ss)
print("Area of a sphere is",h)
print("Permeter of sphere is",tt)
