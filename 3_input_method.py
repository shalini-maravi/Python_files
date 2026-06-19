"""
    - bydefault input() method value is string
    - input() method is user define method
    - value enter by compile time (running program)
"""
## 1 -- Calculate Addition of Three number using input method
""" n1 = input("Enter the first number:")
n2 = input("Enter the second number:")
n3 = input("Enter the third number:")
add = n1 + n2 + n3
print(add) """
#  This input method is use to join both instance vlaue not to calculate value

## 2 --  Calculate Addition of two number using input method from integer
# To perform actual addition we need to write [[int]] before input()
""" n1 = int(input("Enter the first number:"))
n2 = int(input("Enter the second number:"))
add = n1 + n2
print(add) """


## 3 -- Calculate Multiply of two numbers using input method from float
"""n1 = float(input("Enter the first number:"))
n2 = float(input("Enter the second number:"))
mul = n1 * n2 
print(mul) """

## 4 -- calculate Division of two number using input method from float
""" n1 = float(input("Enter the first number:"))
n2 = float(input("Enter the second number:"))
div = n1 / n2 
print(div) """

## -- user input of string value -- 
""" Name = input("Enter your name:")
print("your name:",Name)
#Printing data type of name
print (type(Name)) """

## -- user input of Integer value -- 
#method 1
""" number = input("Enter any number:")
print("Type of number:",type(number))
#converting string into integer
num = int(number)
print("Given Number:",num)
#printing of data type of num
print("Type of number:",type(num)) """

## method 2
""" number = int(input("Enter any number:"))
print("Given Number:",number)
##printing of data type of number
print("Type of number",type(number)) """

## -- user input of float value
marks = float(input("Enter your marks:"))
print("Your marks is:",marks)
print("Type of number:",type(marks))






