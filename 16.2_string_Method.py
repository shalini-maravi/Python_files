# S t r i n g  M e t h o d
# 1. Capitalize()
""" str = "easy softwares"
print(str.capitalize()) """

# 2. Casefold()
""" str="Easy Softwasres"
print(str.casefold) """ 

# Center()
""" str="Easy"
print("Original String;",str)
print("Centered String:",str.center(20)) """

# Example 
""" str="Easy"
print("Original String;",str)
print("Centered String:",str.center(10,"@")) """

# endswith()
""" str="Easy Softwares"
print(str.endswith("softwares"))
print(str.endswith("Softwares")) """

# startswith()
""" str="Easy "
print(str.startswith("easy"))
print(str.startswith("Easy"))
 """

# find()
""" str="you can learn python easily."
print(str.find("python"))
print(str.find("python",10))
print(str.find("python",15))
print(str.find("can",3,10)) """

# index()
""" str="you can learn python easily."
print(str.index("python"))
print(str.index("python",10))
print(str.index("can",3,10)) """

# format()
""" name="Tom"
pro="Python"
print("my name is {} and i lova{}".format(name,pro)) """

# ex:-
""" name="Tom"
pro="Python"
print("my name is {0} and i lova{1}".format(name,pro)) """

# ex:-
""" name="Tom"
pro="Python"
print("my name is {1} and i lova{0}".format(name,pro))
"""

# islnum()
""" str1="easy123"
str2="easy@123"
print(str1.islnum())
print(str2.islnum()) """

# isalpha()
"""str1="easy"
str2="easy@123"
print(str1.isalpha())
print(str2.isalpha()) """


# .isdecimal()
""" str1="easy"
str2="123"
print(str1.isdecimal())
print(str2.isdecimal()) """

# .isdigit()
""" str1="easy"
str2="123"
print(str1.isdigit())
print(str2.isdigit()) """

# isidentifier()
""" str1="easy"
str2="123"
str3="abc123"
str4="*abc*"
str5="ab@cd"
print(str1.isidentifier())
print(str2.isidentifier())
print(str3.isidentifier())
print(str4.isidentifier())
print(str5.isidentifier()) """

# islower()
"""str1="python"
str2="Python"
print(str1.islower())
print(str2.islower()) """

# isnumeric()
"""str1="python"
str2="12345"
print(str1.isnumeric())
print(str2.isnumeric())"""

# isupper()
""" str1="python"
str2="PYTHON"
print(str1.isupper())
print(str2.isupper())
 """
# isspace()
""" str1="   "
str2="Python"
print(str1.isspace())
print(str2.isspace())  """

#len()
""" str1="Easy"
str2="Python"
print("Length of str1:",len(str1))
print("Length of str2:",len(str2))  """

#lower()
""" str1="Easy"
str2="PyTHon"
print("str1:",str1.islower())
print("str2:",str2.islower())  """
 
#upper()
""" str1="Easy"
str2="PyTHON"
print("str1:",str1.islower())
print("str2:",str2.islower())  """

#swapcase()
""" str1="Easy"
str2="PyTHON"
print("str1:",str1.swapcase())
print("str2:",str2.swapcase())  """

#strip()
""" str2="PyTHON"
print("Without strip:",str,"Programming")
print("with strip:",str2.strip(),"Programming")  """

# lstrip()
""" str="PyTHON"
print("Without strip:",str,"Programming")
print("with strip:",str.lstrip(),"Programming") """

#rstrip()
""" str="PyTHON"
print("Without strip:",str,"Programming")
print("with strip:",str.rstrip(),"Programming")  """

# replace()
""" str="I Love Java"
print("Original String:",str)
str=str.replace("java","Python")
print("New String:",str) """

# split()
""" str="I Love Java"
print("Original String:",str)
mylist=str.split();
print("New String:",mylist) """

""" str="I*Love*Java"
print("Original String:",str)
mylist=str.split("*")
print("New String:",mylist) """