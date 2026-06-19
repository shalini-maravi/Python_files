## ------------------- File Handling ------------------------------(Create file in folder)
# Write into a file
""" fileptr = open("D:/easy.txt","w")
fileptr.write("Hello File Handlingn")
fileptr.close() 
 """
#Appending into a file
""" fileptr = open("D:/easy.txt","a")
fileptr.write("\n File Handling is difficult for understand")
fileptr.close()  """

# Reading from a file
""" fileptr = open("D:/easy.txt","r")
filedata=fileptr.read()
print("File data:",filedata)
fileptr.close() """

# Reading 10 bytes from the file
""" fileptr = open("D:/easy.txt","r")
filedata=fileptr.read(10)
print("10 bytes of the File is :",filedata)
fileptr.close() """

# Reading line from the file
""" fileptr = open("D:/easy.txt","r")
line1=fileptr.readline()
print("line1:",line1)
fileptr.close()
 """

# Reading two line from the file
""" fileptr = open("D:/easy.txt","r")
line1=fileptr.readline()
line2=fileptr.readline()
print("line1:",line1)
print("line2:",line2)
fileptr.close() """

# Example: count number of character in a file
""" fileptr = open ("D:/easy.txt","r")
filecontent = fileptr.read()
count = 0
for i in filecontent:
    count = count + 1;
print("Total characters :",count)
fileptr.close() """

# Example : count number of Alphabets in a file
""" fileptr = open ("D:/easy.txt","r")
filecontent = fileptr.read()
count = 0
for i in filecontent:
    if i.isalpha():
        count = count + 1;
print("Total Alphabets:",count)
fileptr.close() """

# Example : count number of Digits in a file
fileptr = open ("D:/easy.txt","r")
filecontent = fileptr.read()
count = 0
for i in filecontent:
    if i.isalpha():
        count = count + 1;
print("Total Alphabets:",count)
fileptr.close() 


