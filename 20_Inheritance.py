### Single Inheritance +Default Inheritance
""" class A:
    x = 10
    def demo1(self):
        print('Value of x :',self.x)
class B(A): #extend + reference
    y = 20
    def demo2(self):
        print('Value of y:',self.y)

# calling
obj1 = B()
obj1.demo1()
obj1.demo2() """

### Using Parameter
""" class A:
    def demo1(self,x,y):
        z = x + y
        print('Addition (x + y):',z)
class B(A):  # extends+ reference
    def demo2(self,a,b):
        c = a - b
        print('Substraction(a-b):',c)

# Calling
obj1 = B()
obj1.demo1(5,3)
obj1.demo2(7,4) """

### MULTIPLE INHERITANCE
""" class fontend:
    def designer(self):
        print("Web Designing")
class backend:  
    def developer(self):
        print("Dynamic Web Pages")
class developer(fontend,backend):  
    def Web_developer(self):
        print("Online Web Develop")
    
dev = developer()
dev.developer()
dev.designer()
dev.Web_developer()
 """

## Creating Class Rectangie
""" class Rectangle:
    def rec_area(self,height,width):
        area=height*width
        print("Area of Rectangle:",area)
class square(Rectangle):
    def squ_area(self,side):
        area=side*side
        print("Area of Square:",area)
    
# Calling
obj=square()
obj.rec_area(10,20)
obj.squ_area(12) """

## Single Inheritance
""" class Rectangle:
    def rec_area(self,height,width):
        area=height*width
        print("Area of Rectangle:",area)
class square(Rectangle):
    def squ_area(self,side):
        area=side*side
        print("Area of Square:",area)
    
# Calling
obj=square()
obj.rec_area(10,20)
obj.squ_area(12) """

## Multiple Inheritance
""" class Rectangle:
    def rec_area(self,height,width):
        area=height*width
        print("Area of Rectangle:",area)
class square:
    def squ_area(self,side):
        area=side*side
        print("Area of Square:",area)
class Triangle(Rectangle,square):
    def tri_area(self,length,breadth):
        area=0.5*length*breadth
        print("Area of Triangle:",area)
    
# Calling
obj=Triangle()
obj.rec_area(10,20)
obj.squ_area(12) 
obj.tri_area(12,25)
 """

## Multilevel Inheritance
""" class Rectangle:
    def rec_area(self,height,width):
        area=height*width
        print("Area of Rectangle:",area)
class square(Rectangle):
    def squ_area(self,side):
        area=side*side
        print("Area of Square:",area)
class Triangle(square):
    def tri_area(self,length,breadth):
        area=0.5*length*breadth
        print("Area of Triangle:",area)
    
# Calling
obj=Triangle()
obj.rec_area(10,20)
obj.squ_area(12) 
obj.tri_area(12,25) """

## Hieracchical Inheritance
""" class Rectangle:
    def rec_area(self,height,width):
        area=height*width
        print("Area of Rectangle:",area)
class square(Rectangle):
    def squ_area(self,side):
        area=side*side
        print("Area of Square:",area)
class Triangle(Rectangle):
    def tri_area(self,length,breadth):
        area=0.5*length*breadth
        print("Area of Triangle:",area)
    
# Calling
obj=Triangle()
obj.rec_area(10,20) 
obj.tri_area(12,25) """

## Hybrid Inheritance
class Rectangle:
    def rec_area(self,height,width):
        area=height*width
        print("Area of Rectangle:",area)
class square:
    def squ_area(self,side):
        area=side*side
        print("Area of Square:",area)
class Triangle(Rectangle,square):
    def tri_area(self,length,breadth):
        area=0.5*length*breadth
        print("Area of Triangle:",area)
class circle(Triangle):
    def cir_area(self,radius):
        area = 3.14*radius*radius
        print("Area of Circle:",area)
    
# Calling
obj=circle()
obj.rec_area(10,20)
obj.squ_area(12) 
obj.tri_area(12,25)
obj.cir_area(2.1)

