""" ## 1 --- Local variable program --- ###
def add():
    x = 3
    y = 7
    print(x + y)
add() # Calling fuction
## -- if we write variable outside function like
#  print(x) it will generate error because we
#  are defining it outside the local variable function
#example --##
print(x) 
 # Calling definition value outside
# NameError: name 'x' is not defined """
 
## 2 --- Global variable program --- ###
""" x = 5 # global variable
def add():
    y = 75 # local variable
    print( x + y)
add()
print("X::",x)
print("y::",y) 
# NameError: name 'y' is not defined """

## 3 --- same variable name of global and local variable --- ###
""" x = 12
def sample():
    x = 42
    print("inside function:",x)
print("outside function::",x)
sample() """

# printing value of variable
#crating variable
""" name = "shanaya"
rollno = 14
marks = 80.40 
# printing value of variable
print("Name:",name)
print("Roll:",rollno)
print("Marks:",marks) """


#Assigning single value to multiple variable
# crating variable
""" a=b=c=80
# printing value of variable
print("a:",a)
print("b:",b)
print("c:",c) """

# Assigning multiple value to multiple variable
#creating variable
""" a=b=c=80
#printing value of variable
print("a:",a)
print("b:",b)
print("c:",c) """

#function definition
""" def add():
    #creating variable
    x = 50
    y = 40
    z = x + y
    print("Add=",z)
    #Calling function
add()
print(x) """

### ---- Global variable ---- ###
# creating global variable
""" x = 69
y = 50
def add():
    #accessing a global variale 
    #inside a function
    print("Inside a function sum=",x+y)
#calling function
add()
# accessing global variable
#  outside a function
print("Outside a function sum=",x+y) """

## ***** Local and Global variable with same name ***** ###
#creating global variable
""" x=50
def add():
    x=20
    #this line will print 20
    print("Inside function x=",x)
    #calling function
add()
#this line will print 50
print("Outside function x=",x) """

#**** GLOBAL VARIABLE ****
x = 50
def add():
    global x
    #updating value of x
    x=20
    #this line will print 20
    print("Inside function x=",x)
    #calling function
add()
    #this line will print 20 
print("Outside function x=",x)














    
