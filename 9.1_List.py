# Acccess value of list using index
"""fruit_list=["Apple","Orange","Mango"]
print("I Like",fruit_list[0])
print("I like",fruit_list[2])
 """
""" int_list=[5,10,15,20,25,30,35,40,45,50]
print("I like",int_list[1:4])
 """
# Access value of list using negative index
""" fruit_list=["Apple","Orange","Mango"]
print(fruit_list[-3])
print(fruit_list[-2])
print(fruit_list[-1])
 """
# Access value of list using positive index
""" fruit_list=["Apple","Orange","Mango"]
print(fruit_list[0])
print(fruit_list[2])
print(fruit_list[1])
 """

# Access value of list using loop
""" fruit_list=["Apple","Orange","Mango"]
for name in fruit_list:
    print("I like",name) """

# update item of list
""" fruit_list=["Apple","Orange","Mango"]
print("Before Updation")
print(fruit_list)
# this line will replace Orange with Banana
fruit_list[1]=["Apple","Orange","Mango"]
print("After Updation")
print(fruit_list) """

#Length of list
""" fruit_list=["Apple","Orange","Mango"]
print("Length of list is ",len(fruit_list)) """

# Add items into list
""" fruit_list=["Apple","Orange","Mango"]
print("Before insertion")
print(fruit_list)
# this line will add the Banana at the end of list
fruit_list.append("Banana")
print("After insertion")
print(fruit_list) """

# Add items at particular index
""" fruit_list=["Apple","Orange","Mango"]
print("Before insertion")
print(fruit_list)
# this line will add the Banana at the end of list
fruit_list.insert(1,"Banana")
print("After insertion")
print(fruit_list) """

# Delete item from list
""" fruit_list=["Apple","Orange","Mango"]
print("Before deletion")
print(fruit_list)
# this line will add the Banana at the end of list
fruit_list.remove("Orange")
print("After deletion")
print(fruit_list) """

# Delete item using index
""" fruit_list=["Apple","Orange","Mango"]
print("Before Deletion")
print(fruit_list)
# this line will add the Banana at the end of list
fruit_list.pop(1)
print("After Deletion")
print(fruit_list) """

# pop()function will delete list Item if we do not pass index
""" fruit_list=["Apple","Orange","Mango"]
print("Before Deletion")
print(fruit_list)
# this line will add the Banana at the end of list
fruit_list.pop()
print("After deletion")
print(fruit_list) """

# del keyword is also used to delete item using index
""" fruit_list=["Apple","Orange","Mango"]
print("Before Deletion")
print(fruit_list)
# this line will add the Banana at the end of list
del fruit_list[1]
print("After deletion")
print(fruit_list)  """

# del keyword is also used to delete all the iteme of list.
""" fruit_list=["Apple","Orange","Mango"]
print("List Item")
print(fruit_list)
# this line will add the Banana at the end of list
del fruit_list
print("Deleted Successfully") """

# Clear list
""" fruit_list=["Apple","Orange","Mango"]
print("Before clear")
print(fruit_list)
# this line will add the Banana at the end of list
fruit_list.clear()
print("After clear")
print(fruit_list)  """

# Copy one list into another
""" list1=["Apple","Orange","Mango"]
print("List1 item")
print(list1)
# this line will add the Banana at the end of list
list2=list1.copy()
print("list2 items")
print(list2) 
  """

# join to list using + symbol
""" list1 = ["Applle","Mango","Orange"]
list2 = ["Cherryt","Grapes","Melon"]
# this line will join list1 and list2
list3 = list1+list2
print("List3 items")
print(list3) """

# join two  list using extend function
""" list1 = ["Apple","Mango","Orange"]
list2 = ["Cherry","Grapes","Melon"]
# this line will add list1 and list2 
list1.extend(list2)
print("list1 item")
print(list1) """

# join two listusing append function
list1 = ["Apple","Mango","Orange"]
list2 = ["Cherry","Grapes","Melon"]
# this line will add list2 item into list 
for name in list2: 
    list1.append(name)
print("list1 item")
print(list1)