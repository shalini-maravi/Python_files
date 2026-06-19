####### | Lambda Function | #######
#-----------------------------------------------------------
#-- add 4 in any values
""" calc = lambda n : n + 4
print(calc(6)) """

#-- Slice Starting 4 characters
""" txt= lambda name: name[5:]
print(txt('maharashtra')) """

#-- print only city name
""" list = ['01 goa','02 wardha','03 gondia' ]
txt1 = lambda name: name[3:]

for i in list:
    print(txt1(i))
 """
#-- print square of numbers list
""" list1 = [6,3,4,7,2,8,9]
sqr = lambda n : n ** 2
for i in list1:
    print(sqr(i)) """

#-----------------------------------------------------------
#============= | -- PDF EXAMPLES -- | ============
#-----------------------------------------------------------

#What are Lambda Functions in Python? 
""" Lambda Functions in Python are anonymous functions, implying they don't have a 
name. The def keyword is needed to create a typical function in Python, as we 
already know. We can also use the lambda keyword in Python to define an unnamed 
function """

#Example 1:

#code to demonstrate how we can use a lambda 
#function for adding 4 number
""" add = lambda num: num + 4
print(add(6)) """

#Example 2:
""" Now we gave an example of a lambda function that adds 4 to the input number using 
the add function. The code is shown below -  """

""" def add(num):
    return num + 4
print(add(6)) """

#Example 3: 
""" Now we gave an example of a lambda function that multiply 2 numbers and return 
one result. The code is shown below - """

""" a = lambda x, y : (x * y)
print(a(4,5)) """

#Example 4:
""" Now we gave another example of a lambda function that adds 2 numbers and return 
one result. The code is shown below - """

""" a = lambda x,y,z : (x + y + z)
print(a(4,5,5)) """

#----------------------------------------------------------------------------------------------------------
##==== What's the Distinction between Lambda and def functions? ====###
#----------------------------------------------------------------------------------------------------------
""" Let's glance at this instance to see how a conventional def defined function 
differs from a function defined using the lambda keyword. This program calculates 
the reciprocal of a given number:  """


# --Python code to show the reciprocal of the given number to highlight the
# difference between def() and lambda(). --#
""" def reciprocal(num):
    return 1/num
lambda_recipocal = lambda num: 1/num
# using the function defined by def keyword
print("Def keyword:",reciprocal(6))
# using the function defined by lambda keyword
print("Lambda keyword:", lambda_recipocal(6)) """

##-- Using Lambda Function with filter()
""" 
The filter() method accepts two arguments in Python: a function and an iterable 
such as a list. 
Here we give an example of lambda function with filter() in Python. The code is 
given below - 
"""

##-- This code used to filter the odd number from the given list
""" list_ = [35,12,69,55,75,14,73]
odd_list= list(filter(lambda num:(num%2!=0),list_))
print('This List of odd number is:,odd_list') """

##-- Using Lambda Function with map() 
#A method and a list are passed to Python's map() function.
#Code to calculate the square of each number of a list using the map() function 

""" numbers_list = [2,4,5,1,3,7,8,9,10]
squared_list = list(map(lambda num: num ** 2,numbers_list))
print('square of each number in the given list:', squared_list) """

##-- Using Lambda Function with List Comprehension 
#Code to calculate square of each number of lists using list comprehension 

""" squares = [lambda num = num: num ** 2 for num in range(0,11)]
for square in squares:
    print('This square value of all number from 0 to 10:', square(),end=" ") """

##-- Using Lambda Function with if-else 
"""  In the program code 
below, we check which number is greater than the given two numbers using the if
else block.  """

#  Code to use lambda function with if-else 
""" minimum = lambda x,y: x if(x<y) else y
print('This greater number is:, minimum(35,75)') """

##-- Using Lambda with Multiple Statements 
# Code to print the third largest number of the 
# given list using the lambda function   

my_List = [[3,5,8,6],[23,54,12,87],[1,2,4,12,5]]
#sorting every sublist of the above list
sort_List = lambda num: (sorted(n) for n in num)
# Getting the third largest number of the sublist
third_Largest = lambda num, func:[L[len(L)-2]for L in func(num)]

result = third_Largest(my_List,sort_List)
print('The third largest number from every sub list is:',result)





