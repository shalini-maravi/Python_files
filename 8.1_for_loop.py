### Structure of for loop
'''
for a in range(1,20,2):
    print(a)
'''    

'''
### for loop with string
str="Easy"
for x in str:
    print(x)
'''
'''
### for loop with list
student = ["Ravi","Rocky","Amisha"]
for x in student:
    print (x)
'''

'''
### Table of any number
no=int(input("Enter any number:")) 
print("Table of",no,"is given below")
for i in range(1,11):
    print(i*no)
'''
### for loop with else
### Example 1)
'''
Student = ["Amisha","Rinkal","mahima"]
for name in Student:
    print(name)
else:
    print("This is else block")
'''
 
### for loop with else
### Example 2)
Student = ["Amisha","Rinkal","Mahima"]
for name in Student:
    if name == "Rinkal":
        break
    else:
        print (name)
else:
    print("This is else Block")
    


