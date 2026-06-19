# create tuple list
""" t1 = (1,2,3,4)
print(t1)
print(type(t1))
t2 = 1,2,3,4
print(t2)
print(type(t2)) """


# tuple create mixed data ?
""" tuple_mix = (1,4,"Code",True,None,4,"Deep")
print(tuple_mix)
print({1,4,"Code",True,None,4,"Deep"})

print("Data Type of tuple_mix:",type(tuple_mix))
print("Data Type of new Data:",type({1,4,"Code",True,None,4,"Deep"})) """

# find the Length of Tuple
""" tuple_mix = (1,4,"Code",True,None,4,"Deep")
print(len(tuple_mix)) """


tuple_mix = (1,4,"Code",True,None,4,"Deep")
print(tuple_mix)
data = tuple_mix[3]
print(data)

# Copy one Touple Variable to another variable
var = 1,2,3,4,True,"Like"
l = var.index(4)
print(l)

# Find Index Value of Touple
var = 1,2,3,4,True,"Like"
var2 = var
print(var2)