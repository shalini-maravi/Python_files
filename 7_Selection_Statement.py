"""
    1. only if
    2. if else
    3. nested if else
    4. ladder if else
"""

## If statement ##
#-------------------------------------------------------
# Example 1:
""" no = int(input("Enter any number:"))
if no>5:
    print("Number is greater than 5") """

# Example 2:
""" no = int(input("Enter any number:"))
if no>0:
    print("Number is positive")
if no<0:
    print("Number is negative")
if no==0:
    print("Number is zero") """




##  if_else Statement
#------------------------------------------------------
# 1. Positive Negative numbers
# 2. Find the Profit or Loss

""" num = int(input("Enter the number::"))
if num>0:
    print("positive")
else:
    print("negative") """


""" pur_price = int(input("Enter the purchase price::"))
sal_price = int(input("Enter the sale price::"))
if pur_price < sal_price:
    print("profit")
else:
    print("lose") """


# Position of Condition
'''------------------------------------------
    1 is True condition         true expression
    0 is false condition        false expression

if 1:
    print("Accepted..")
else:
    print(".....")

'''

# Ex.1
""" no = int(input("Enter any number:"))
if no>5:
    print("Number is greater than 5")
else:
    print("Number is less than 5") """

#Ex. 2
""" if 10:
    print("Hello")
else:
    print("Hi") """

#Ex. 3
""" if 0:
    print("Hello")
else:
    print("Hi") """

# Ex. 4
""" 
if 'A':
    print("Hello")
else:
    print("Hi") """

# EXAMPLE 2:
""" no = int(input("Enter any number:"))
if no%2==0:
    print("Number is even")
else:
    print("Number is odd") """



## - Ladder if-else Statement
# ----------------------------------------------------------
# 1. Check the numbers is greater/ less/ equals
# 2. find the grade

""" n1 = 12
n2 = 69
if n1>n2:
    print(n1,"is greater than",n2)
elif n1<n2:
    print(n1,"is less than",n2)
elif n1==n2:
    print(n1,"is equal to",n2)
else:
    print("Wrong Input...?") """

# A = 90 | B = 65 | C = 45 | D = 35 | FAILED
""" 
per = 36 
if per >= 90:
    print("A")
elif per >= 65:
    print("B")
elif per >= 45:
    print("C")
elif per>=35:
    print("D")
else:
    print("failed") """

# Example 1:
""" no = 7
if no>10:
    print("Hello1")
elif no>5:
    print("Hello2")
elif no>0:
    print("Hello3")
else:
    print("Hello4") """

# Example 2:
""" no = -5
if no>10: 
    print("Hello1") 
elif no>5: 
    print("Hello2") 
elif no>0:  
    print("Hello3") 
else: 
    print("Hello4") """ 

# Example 2 : Show result according to percent
""" 
percent = float(input("Enter your percentage:"))
if percent >= 60:
    print("First division")
elif percent >= 45:
    print("Second division")
elif percent >= 33:
    print("Third division")
else:
    print("Sorry!!! you are fail.") """

### NESTED IF STATEMENT ### 
# Example 1
""" 
no = 5
if no>2:
    if no<3:
        print("Hello")
    print("Hi") """

# Example 2
""" no = 5
if no>2:
    if no>3:
        print("Hello")
    print("Hi") """


# Example 3
""" no=5 
if no<2:
    if no>3:
        print("Hello")
    print("Hi") """

# Example 2: Find Greatest value in three number
""" 
print("Enter three number:")
a=int(input())
b=int(input())
c=int(input())
if a>b:
    if a>c:
        print(a,"is greatest")
if b>a:
     if b>c:
        print(b,"is greatest")
if c>a:
     if c>b:
         print(c,"is greatest") """



        
