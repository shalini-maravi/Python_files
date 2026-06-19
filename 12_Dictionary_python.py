# // Empty dictionary
""" var = {}
print(type(var)) """

# // dictionary method
""" var = dict()
print(type(var)) """

# // dict() method set the value in key pair form
""" var = {"name":"ankit","Age":22}
print(type(var))
print(var) """

# // dict() method set the value in some data-type
""" var = {"name":"ankit","Age":22,"username":"ruby"}
print(type(var))
print(var) """

# // dict() method set the value in some key 
""" var = {"name":"ankit","Age":22,"name":"ruby"}
print(type(var))
print(var)  """

# // capture the key value using list"[]" index 
""" var = {"name":"ankit","Age":22,"name":"ruby"}
print(type(var))
print(var["name"]) """ 

# // pop()method- print the currospond value
""" var = {"name":"ankit","Age":22,"name":"ruby","Password":"code1234"}
var.pop("name") """

# // get()method- print the currospond value
""" var = {"name":"ankit","Age":22,"name":"ruby","Password":"code1234"}
print(var.get("password"))
 """

# // get()method- print the Unknown value
""" var = {"name":"ankit","Age":22,"name":"ruby","Password":"code1234"}
print(var.get("pass")) """

# // clear()method- clear the all value
""" var = {"name":"ankit","Age":22,"name":"ruby","Password":"code1234"}
var.clear()
print(var)
 """

# // keys()method- all key to show
"""var = {"name":"ankit","Age":22,"name":"ruby","Password":"code1234"}
print(var.keys())
 """

# // items()method- All dictionary item to show
""" var = {"name":"Ankit","Age":22,"name":"ruby","Password":"code1234"}
print(var.items()) """


# // item()method Another Example
""" var = {"name":"ankit","Age":22,"name":"ruby","Password":"code1234"}
for key, value in var.items():
    print(key,value,sep=" - ") """
 
# // Update the value in seprate position
var = {"name":"ankit","Age":22,"name":"ruby","Password":"code1234"}
var["Age"]=25
print(var) 