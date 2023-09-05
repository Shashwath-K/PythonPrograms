import math

class Shape:
    def __init__(self):
        self.area=0
        self.name=""
    def showArea(self):
        print("The area of the", self.name,"is",self.area,"units")

class circle(Shape):
    def __init__(self,radius):
        self.area=0
        self.name="circle"
        self.radius=radius
    def calcArea(self):
        self.area=math.pi*self.radius*self.radius

class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.area=0
        self.name="Rectangle"
        self.length=length
        self.breadth=breadth
    def clacArea(self):
        self.area=self.length*self.breadth

class Triangle(Shape):
    def __init__(self,base,height):
        self.area=0
        self.name="Triangle"
        self.base=base
        self.height=height
    def clacArea(self):
        self.area=(self.base*self.height)/2

c1=circle(5)
c1.calcArea()
c1.showArea()

r1=Rectangle(5,10)
r1.clacArea()
r1.showArea()

t1=Triangle(6,12)
t1.clacArea()
t1.showArea()
