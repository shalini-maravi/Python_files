# len()
""" print("this is a print function")
print(len("Something")) """

# User-define Function:-

# example 1:-
""" a = 8
b = 4
print("Addition:",8+4)
print("Substraction:",8-4)
print("Multiplication:",8*4)
print("Division:",8/4)
 """
#Example :-2
""" a = 7
b = 13
print("Addition:",a+b)
print("Substraction:",a-b)
print("Multiplication:",a*b)
print("Division:",a/b) """

# Using Function----------------
# Example :-1
""" def calculator(a,b):
    print("Addition:",a+b)
    print("Substraction:",a-b)
    print("Multiplication:",a*b)
    print("Division:",a/b)
# function calling
calculator(8,4) """

# Example :-2
""" def greeting():
    print("Good Morning")
#function calling
print(greeting()) """

# Example :-3
""" def greeting():
    print("Good Morning")
msg=greeting()
#function calling
print(msg) """

# Example :-4
""" def greeting(name):
    print("Good Morning",name)
greeting("Codeblock") """

# TYPE FUNCTION ARGUMENT
# ----------------------------------
# position
""" def greeting (fname,lname):
    print("Good Evening",fname,lname)
greeting("code","Block") """

# keyword
""" def greeting (fname,lname):
    print("Good Evening",fname,lname)
greeting(fname="code",lname="Block") """

# default Argument
# Example :-1
""" def greet (fname="guest"):
    print("Good Evening",fname)
greet()
 """

# Example :-2
""" def greet (fname="guest"):
    print("Good Evening",fname)
greet("Roy")
 """

# Variable Length Argumenr:-
""" def test (*args):
    print(args)
    print(len(args))
    print(type(args))
test("india","Shri lanka","US")
 """
# Using Keyword Argument:-
# Example 1:-
def test (**kwargs):
    print(kwargs)
    print(len(kwargs))
    print(type(kwargs))
test (country = "india",fname="Shri lanka",lname="US")
