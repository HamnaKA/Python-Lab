area_square = lambda side : side * side
area_rectangle = lambda length,width : length * width
area_triangle =  lambda s,a,b,c : (s*(s-a)*(s-b)*(s-c)) ** 0.5

a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
c=int(input("enter the value of c:"))
s = (a + b + c) / 2

print("area of square:",area_square(a))
print("area of rectangle:",area_rectangle(a,b))
print("area of triangle:",area_triangle(s,a,b,c))
