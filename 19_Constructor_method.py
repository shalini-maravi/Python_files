""" class flower:
    def __init__(self):
        print('This is self method')

obj = flower() # no need to call a function """


## parameterized Constructor
""" class flower:
    def __init__(self, rno, name):
        print("Roll no.: ",rno)
        print("Name :",name)
obj = flower(12,'ANI') """


## non-parameterized Constructor
"""class machine:
    def __init__(self):
        print('V-Tech Computer Institute')
    def course(self):
        cor = 'TallyPrime'
        fess = 5400
        print('Course Name :',cor)
        print('Fees: ',fess)
m1 = machine()
m1.course() """

#  ------------------------------Conctructor Method-----------------------------------
""" class flower:
    def __init__(self):
        print("This is self Method.")

obj = flower()  # no need to call a function """

""" # Parameterized Constructor
class flower:
    def __init__(self):
        print("This is self Method.")

obj = flower()  # no need to call a function
 """

# Non-Parameterized Constructor
""" class machine:
    def __init__(self):
        print("This is a Machine.")
    def course(self):
        cor = 'Python'
        fees = 4500
        print('course name',cor)
        print('Fees ',fees)
obj = machine()  # no need to call a function
m1=machine()
m1.course() """

# Creating Class-------------
""" class Student:
    def __init_(self):
        print("Hi I am non-Parameterized Constructor")
    def Info(self):
        print("Name:Aayushi")
        print("Roll no:305")
s1=Student()
s1.Info() """

class Student:
    def __init__(self,name,roll):
        print("Name:",name)
        print("Roll no:",roll)

s1 = Student('Ayushi',305)
