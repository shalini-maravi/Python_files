##  Normal Example-------------
""" class A:
    x = 10
    y = 20
    def demo1(self):
        print("This is method 1")
class B(A):
    def demo2(self):
        print("This is method 2")
# Calling Object
obj = B()
obj.demo1()
obj.demo2() """

## With data hiding i.e data abstraction--------
""" class A:
    __x = 10
    y = 20
    def demo1(self):
        print("This is method 1")
        print("X:",self.__X)   ##AttributeError: 'B' object has no attribute '_A__X'. Did you mean: '_A__x'?
class B(A):
    def demo2(self):
        print("This is method 2")
        print(self.y)
# Calling Object
obj = B()
obj.demo1()
obj.demo2() """

## 
""" class A:
    __x = 10
    y = 20
    def demo1(self):
        print("This is method 1")
class B(A):
    def demo2(self):
        print("This is method 2")
        print(self.x)    ## AttributeError: 'B' object has no attribute '_A__X'. Did you mean: '_A__x'?  
# Calling Object
obj = B()
obj.demo1()
obj.demo2() """


###---------------- D A T A  A B S T R A C T I O N ---------------------

# Normal Example
""" class Test1:
    x = 10
    y = 20
    def myfun1(self):
        print("This is Function1")
class Test2(Test1):
        def myfun2(self):
            print("This is Function2")
            print(self.x)
            self.myfun1()
# calling function
obj = Test2()
obj.myfun2() """

# Example with data Hiding----------
class Test1:
    __x = 10           # AttributeError: 'Test2' object has no attribute 'x'
    y = 20
    def myfun1(self):
        print("This is Function1")
class Test2(Test1):
        def myfun2(self):
            print("This is Function2")
            print(self.x)
            self.myfun1()
# calling function
obj = Test2()
obj.myfun2()