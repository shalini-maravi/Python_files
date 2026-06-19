########## | Jump Statement | ##########

"""
It is used to transfer the control from one point to another point in 
the program. 
"""

# 1.break statement
# 2.continue statement

######### -- 1. break statement -- #########
""" ▪ It is used to transfer the control out of the body of loop. 
▪ In other word we can say that it terminates the current loop. 
▪ break statement are mostly used with loop(for loop or while loop).  """

# Example 1: program without break
""" for i in range(1,11):
    print(i,end=" ") """

#Example 2: Same program with break
""" for i in range(1,11):
    if i == 5:
        break
    else:
        print(i,end=" ") """

#--------------------------------------------------------------------------------------------
######### -- 2. continue statement -- #########
"""
▪ It is used to skip the next statement and continue the loop. 
▪ continue statement are mostly used with loop(for,while).  
"""

#Example 1:
for i in range(1,11):
    if i == 5:
        continue
    else:
        print(i,end=" ")

#Example 2:
for i in range(1,11):
    if i>=5:
        continue
    else:
        print(i,end=" ")

#Example 3:
for i in range(1,11):
    if i<=5:
        continue
    else:
        print(i,end=" ")

#Example 4:
for i in range(1,11):
    if i!=5:
        continue
    else:
        print(i,end=" ")





