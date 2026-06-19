# 1) Empty Set
""" var = {}
print(type(var)) """
# 2) Perfect Empty Set
""" var = set()
print(type(var)) """
# 3) Perfect Empty Set but element given
""" var = set("1")  # only one element execute
print(type(var)) """
#--------------------------------------------------------#
# 4) Valu assign in set Variable
""" var = {10,'anii',56.8,True}
print(type(var))
print (var)  """
# 5) Indexing is not allowed in set
""" var = {10,'anii',56.8,True}
print(type(var))
print (var[2])
#TypeError: 'set' object is not  subscriptable """
# 6) Traversing a set
""" s = {1,2.3,"Hello",(2,3)}
for item in s:
    print(item) """
#  7) clear() method
""" var = {10,'ani',56.3,True,'ani'}
var.clear()
print(var) """
# 8) Unique value assign a set
""" var = {10,'ani',56.7,True,'ani'}
print(type(var))
print(var) """
# 9) Mutable operation:
# add ()method
""" var = {10,'ani',56.7,True,'ani'}
var.add("code")
print(var) """
# 10) Update() method
""" var = {10,'ani',56.7,True,'ani'}
var.update("code")
print(var) """
# 11) Update() method
# Example
""" var = {10,'ani',56.7,True,'ani'}
var.update(["code","block"])
print(var) """
# 12) pop() method
""" var = {10,'ani',56.7,True,'ani'}
print(var.pop()) """
# remove()method
""" var = {10,'ani',56.7,True,'ani'}
var.remove(56.7)
print(var) """
# discard()method
""" var = {1,2,3}
var.discard(4)
print(var) """
# copy()meyhod
""" var1 = {1,2,3}
var2 = var1.copy()
print(var2) """
# // Mathamatical Method of python set

# union()method
""" var = {10,'ani',45.3,True}
var2 = {10,'ani',45.6,True,'code',12,False}
print(var.union(var2))
 """
# union()method achive by operator
""" var = {10,'ani',45.3,True}
var2 = {10,'ani',45.6,True,'cody',12,False}
print(var | var2)
 """
# intersection()method
""" var = {10,'ani',45.3,True}
var2 = {10,'ani',45.6,True,'cody',12,False}
print(var.intersection(var2)) """
# intersection()method achieve by operator
""" var = {10,'ani',45.3,True}
var2 = {10,'ani',45.3,True,'cody',12,False}
print(var & var2) """
# difference()method
""" var = {10,'ani',45.3,True,'cody',12,False}
var2 = {10,'ani',45.3,True}
print(var.difference (var2)) """
# difference()method achieve by operator
""" var = {10,'ani',45.3,True,'cody',12,False}
var2 = {10,'ani',45.3,True}
print(var -var) """
# symmetric difference() method
""" var = {10,'ani',45.3,True,'cody',12,False}
var2 = {10,'ani',45.3,True}
print(var.symmetric_difference(var2)) """
# issubset()method
""" a = {1,2}
b = {1,2,3}
print(a.issubset(b)) """
# issuperset()method
a = {1,2}
b = {1,2,3}
print(a.issuperset(b)) 

# isdisjoint()method
""" a = {1,2,3}
b = {3,4,6} """
""" # setComprehension
squares = {x*x for x in range(1,6)}
print(squares) """