""" class A: # old Programming paste
    def demo1(self,var = 12):
        print("Hello")
        print(var)
class B(A):  # new Programming with same Structure of old Programming
    def demo1(self,var = 14):
        print("Hi")
        print(var)
obj = B()
obj.demo1() """

## Online Scrap search---------- (search Programm)

# Defining base class
class Test1:
    def myfun(self):
        print("Base class Function")
# defining derive class
class Test2(Test1):
        def myfun(self):
            print("derive class Function")
# calling function
obj = Test2()
obj.myfun() 