########### | Class and Object | ###########

#---- | Program 1 | ---- #
## creating class
""" class employee:
    #Data Members
    emp_id = 100
    emp_name = 'vaishnavi mange'

    # members function
    def info(self):
        print(self.emp_id)
        print(self.emp_name)

## creating class object
emp1 = employee()
emp1.info() # calling class inside function """
#-----------------------------------------------------------------------

#---- | program 2 | ----#
# create class by login details
class login:
    u_id = 'diana123'
    u_pass = '1234'

    def report(self):
        print("user id:",self.u_id)
        print("user password:",self.u_pass)

obj1= login()
obj1.report()
print("specific print user Id")
print(obj1.u_id)

#------------------------------------------------------------------------
#------------- PDF Example --------------#

#--creating class
""" class student:
    #defining class variables
    name= "Radha"
    roll= 205 """



#-- Accessing variable of class
#creating class
""" class student:
    #defining class variables
    name="Rocky"
    roll=205

#creating object
s1=student()
#Accessing class variable
print("Name:",s1.name)
print("Rollno:",s1.roll) """



##-- class with variable and function
""" #creating class
class student:
    #defining class variable
    name ="Rocky"
    roll=205
    marks=85.6
    #defining function
    def showInfo(self):
        print("Name:",self.name)
        print("Rollno:",self.roll)
        print("Marks:",self.marks)

#creating object
s1= student()
#calling function of class
s1.showInfo() """