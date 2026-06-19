# create a tuple
var =()
print(type(var))

# create a tuple with items
var ={1,2,3,4,5}
print(var)

# create tuple with different types of items
var = (1,2,3,4,5,True,"like")
print(var)

# create tuple using without parantesiis
var = 1,"Like"
print(var)

# check data type of item
var = 1,"Like"
print(type(var))

# copy one tuple variable to another variable
var = 1,2,3,4,True , "Like"
l = var.index(4)
print(l)

# find index value of tuple
var = 1,2,3,4,True , "Like"
var2 = var
print(var2)

""" # Tuple is Immutable
var = 1,2,3,4,True , "Like"
var[1] = "Right"
print(var)
#'tuple' object does not support item assignment
 """
""" # AttributeError
var = 1,2,3,4,True,"Like"
var.append("Right")
print(var)
#'tuple' object has no attribute 'append'


 """
