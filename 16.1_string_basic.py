# string python-----
""" str = "python"
print("string:",str)
print("First character:",str[0])
print("Second character:",str[1])
print("Last character:",str[2])
 """
# access character from string----
""" str="i love python"
print("String:",str)
print("Str[2:6]:",str[2:6])
print("Str[7:-1]:",str[7:-1])
 """
##----
""" str="python"
print(str[0:6])
 """
## Update String
""" str = "Python Programming"
print("Original string:",str)
str = "Java Programming"
print("Update String:",str) """

## Creating String
""" str = "Python Programming"
print("Original string:",str)
str[0] = "m"
print("Update String:",str)
TypeError: 'str' object does not support item assignment """
'''
# Multiline String
str = """ hi jyoti
    hi krisha
    hi shalini
"""
print("Multiline string:",str)

## Example 2
str = """ Hello friend.
you can learn python easily
""" 
print("Multiline string:",str)
'''
 ## search String----
""" str="I lone python Programming"
search_str=input("Enter any string to search:")
if search_str in str:
    print(search_str,"is present")
else:
    print(search_str,"is not present") """

#Example 2:-
""" str = "I love python programming"
search_str =input("Enter any string to search :")
if search_str in str:
    print(search_str,"is present")
else:
    print(search_str,"is not present")
 """

# creating string
""" str = "I love python programming"
print("java" not in str)
print("python" not in str) """

# String Concatenation
str1="I love"
str2="Python Programming"
str3=str1+str2
print("String1:",str1)
print("String2:",str2)
print("String3:",str3)