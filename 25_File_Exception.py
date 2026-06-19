# mismatch error
""" age = input('Enter the age :')
print(type(age))
if age > 18:
    print('accept')
print('End the program') """

# file not found exception
""" fileptr = open("D:\\easy.txt",'r') """

# ZeroDivisionError
""" a = 10
b = 0
print(a/b) """

# Indentation Error
""" if 5 > 10:
print('Good News') """

# mismatch error / Exception Handling
""" try:
    age = input('Enter the age :')
    print(type(age))
    if age > 18:
        print('accept')
except:
        print('Age datatype error..!')
else:
    print('End the Program')
print('Exception Handeling') """

# Example
try:
    a = 10
    print("Value of x:",a)
except:
    print("An exception")
