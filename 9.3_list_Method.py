# 1) append()
"""
fruit_list=["Apple","Mango","Orange"]
print("Fruits list :",fruit_list) 
#this line will add Cherry at the end of list 
fruit_list.append("Cherry")
print("New Fruits list :",fruit_list)
 """
# 2) clear()
""" fruit_list=["Apple","Mango","Orange"]
print("Fruits list :",fruit_list) 
#this line will add Cherry at the end of list 
fruit_list.clear()
print("New Fruits list :",fruit_list) """

# 3) count()
""" Number_list=[10,33,20,30,40,50,33,60,20,70,80,90,20,100]
print("Number list :",Number_list) 
print("Total count of 20 :",Number_list.count(20)) """

# 4) copy()
""" list1=["Apple","Mango","Orange"]
print("list1 item :",list1) 
#this line will copy list1 item into  
list2=list1.copy()
print("list2 items :",list2) """

# 5) extend()
""" list1 = ["Apple","Mango","Orange"]
list2 = ["Cherry","Grapes","Melon"]
# this line will join list1 into list2
list1.extend(list2)
print("list1 item")
print(list1) """

# 6) index()
""" Number_list=[30,46,10,37,93,16,34,16,26,31,70,10,40]
print("Index of 10 :",Number_list.index(10)) """

# 7) insert()
""" fruit_list = ["Apple","Mango","Orange"]
print("Before Insertion")
print(fruit_list)
# this line will add banana at index 1
fruit_list.insert(1,"Banana")
print("After Insertion")
print(fruit_list) """

# 8) pop()
""" fruit_list=["Apple","Mango","BAnana","Cherry"]
print("fruits list :",fruit_list)
# this line will delete last element cherry
fruit_list.pop()
print("Fruits list :",fruit_list)
fruit_list.pop(1)
print("fruits list :",fruit_list) """

# 9) remove()
""" fruit_list = ["Apple","Mango","Orange"]
print("Before Deletion")
print(fruit_list)
# this line will Delete Orange fron list
fruit_list.remove("Orange")
print("After Deletion")
print(fruit_list) """

# 10) reverse()
fruit_list=["Apple","Mango","Banana","Cherry"]
print("fruits list :",fruit_list)
# this line will reverse the list items
fruit_list.reverse()
print("Fruits list :",fruit_list)
print("Reverse fruits list :",fruit_list)

# 11) sort()
## Example 1Ascending order---
str_list =["Apple","Mango","Orange","Cherry"]
int_list =[2,12,32,87,18,41]
char_list=['E','A','S','Y']
print("List Item before sorting")
print(str_list)
print(int_list)
print(char_list)
str_list.sort()
int_list.sort() 
char_list.sort()
print("List Item After sorting")
print(str_list)
print(int_list)
print(char_list)

## Example 2 Descending order---
str_list =["Apple","Mango","Orange","Cherry"]
int_list =[2,12,32,87,18,41]
char_list=['E','A','S','Y']
print("List Item before sorting")
print(str_list)
print(int_list)
print(char_list)
str_list.sort(reverse=True)
int_list.sort(reverse=True) 
char_list.sort(reverse=True)
print("List Item After sorting")
print(str_list)
print(int_list)
print(char_list)