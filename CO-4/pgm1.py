""" Create  Rectangle  class  with  attributes  length  and  breadth
and  methods  to  find  area  and perimeter. 
Compare two Rectangle objects by their area. """

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return (self.length * self.breadth)

    def periemeter(self):
        return (2 * (self.length + self.breadth))


l1 = int(input("enter length1:"))
b1 = int(input("enter breadth 1:"))
r1 = Rectangle(l1, b1)
print("area of rectangle 1:",r1.area())
print("periemeter of rectangle 1:",r1.periemeter())
l2 = int(input("enter length 2:"))
b2 = int(input("enter breadth 2:"))
r2 = Rectangle(l2, b2)
print("area of rectangle 2:",r2.area())
print("periemeter of rectangle 2:",r2.periemeter())
a1=r1.area()
a2=r2.area()
if a1 > a2:
    print("area of rectangle 1 is high")
elif a1 == a2:
    print("area are equal")
else:
    print("area of rectangle 2 is high")
