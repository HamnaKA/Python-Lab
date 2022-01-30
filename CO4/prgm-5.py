class publisher:
    def __init__(self,name):
        self.name=name
    def displayName(self):
        print("Name of Publisher:",self.name)
class book(publisher):
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def displayName(self):
        print("Title of Book:",self.title)
        print("The Author of Book:",self.author)
class python(book):
    def __init__(self,price,npages):
        self.price=price
        self.npages=npages
    def displayName(self):
        print("price of book:",self.price)
        print("Number of pages:",self.npages)
n=input("Enter Name of Publisher:")
a=input("Enter the title of book:")
b=input("Enter the Author of Book:")
c=int(input("Enter the price of the book:"))
d=int(input("Enter the Number of pages:\n"))
s=publisher(n)
m=book(a,b)
n=python(c,d)
s.displayName()
m.displayName()
n.displayName()
