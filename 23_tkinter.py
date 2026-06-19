########## | tkinter | ############# (NOT SO IMPORTANT)
#--------------------------------------------------------------------------
#1. Tkinter is GUI library for Python. 
#2. It is used to create graphical user interface for desktop application. 

""" #importing tkinter
import tkinter
#creating object
top = tkinter.Tk()
#code to add widgets will go here...
#calling mainloop
top.mainloop() """


#Set Dimension of GUI Window  
""" import tkinter
top = tkinter.Tk()
#setting dimension of window
top.geometry("325x200")
top.mainloop() """

#Set title and background color of GUI Window 
""" import tkinter
top = tkinter.Tk()
#setting dimension of window
top.geometry("325x200")
#setting title of window
top.title("Easy")
#setting background color
top['bg']="#51E1DC"
top.mainloop() """

############ | Label | #############
""" from tkinter import * 
top = Tk() 
#window dimension 
top.geometry("300x250") 
top['bg']="#51E1DC" 
# creating label 
uname = Label(top, text="This is a label").place(x=30, y=50) 
top.mainloop() """

########### | Button | #############

""" from tkinter import * 
top = Tk() 
#window dimension 
top.geometry("300x150") 
top['bg']="#51E1DC" 
# creating button 
btn = Button(top, text="Click Me").pack() 
top.mainloop()  """

##--Button with userdefined position 
""" from tkinter import * 
top = Tk() 
#window dimension 
top.geometry("300x150") 
top['bg']="#51E1DC" 
#here x is distance from left 
#and y is distance from top 
btn1 = Button(top, text="Click Me").place(x=50,y=30) 
top.mainloop()  """

##--Call Function on Button click 
""" from tkinter import messagebox 
from tkinter import * 
top = Tk() 
#window dimension 
top.geometry("300x150") 
top['bg']="#51E1DC" 
#creating function 
def myfun(): 
    messagebox.showinfo("Title","You clicked on button") 
btn1 = Button(top, text="Click Me",command=myfun).pack() 
top.mainloop()  """

############## | Entry | #############

""" from tkinter import * 
top = Tk() 
#window dimension 
top.geometry("300x150") 
top['bg']="#51E1DC" 
label = Label(top, text="First Number",).place(x=50,y=50) 
#create text box 
ent=Entry(top).place(x=150,y=50) 
top.mainloop()  """

 
##--Add two numbers 
""" from tkinter import  messagebox 
from tkinter import * 
top = Tk() 
#window dimension 
top.geometry("300x180") 
top['bg']="#51E1DC" 
#defining function 
def add(): 
    f=firstNum.get() 
    s=secondNum.get() 
    messagebox.showinfo("Sum",(f+s)) 
#declaring variables 
firstNum=IntVar() 
secondNum=IntVar() 
#create labels 
Label(top, text="First Number",width="13").place(x=50,y=50) 
Label(top, text="Second Number",width="13").place(x=50,y=90) 
#create text boxes 
Entry(top,textvariable=firstNum).place(x=150,y=50) 
Entry(top,textvariable=secondNum).place(x=150,y=90) 
#create button 
Button(top,text="Add",width="5",bg="orange",command=add).place(x=100,y=120) 
top.mainloop()  """

############## | Button | ###############

""" from tkinter import * 
top = Tk() 
#window dimension 
top.geometry("300x180") 
top['bg']="#51E1DC" 
#create check boxes 
Checkbutton(top,text="Apple",width="15",onvalue=1,offvalue=0).place(x=10,y=20) 
Checkbutton(top,text="Orange",width="15",onvalue=1,offvalue=0).place(x=10,y=50) 
Checkbutton(top,text="Cherry",width="15",onvalue=1,offvalue=0).place(x=10,y=80) 
top.mainloop()  """


##--Print Selected Checkboxes Text 
""" from tkinter import  messagebox 
from tkinter import * 
top = Tk() 
#window dimension 
top.geometry("300x180") 
top['bg']="#51E1DC" 
def fun(): 
    str="" 
    if chk1.get()==1: 
        str=str+ " Apple " 
    if chk2.get()==1: 
        str=str+" Orange " 
    if chk3.get()==1: 
        str = str + " Cherry " 
    messagebox.showinfo("Result",str+" selected") 
chk1=IntVar() 
chk2=IntVar() 
chk3=IntVar() 
#create check boxes 
Checkbutton(top,text="Apple",variable=chk1,width="15",onvalue=1,offvalue=0).pla
ce(x=10,y=20) 
Checkbutton(top,text="Orange",variable=chk2,width="15",onvalue=1,offvalue=0).pl
ace(x=10,y=50) 
Checkbutton(top,text="Cherry",variable=chk3,width="15",onvalue=1,offvalue=0).pl
ace(x=10,y=80) 
Button(top,text="CLICK",command=fun).place(x=15,y=110) 
top.mainloop()  """

############# | Tkinter | ##############

""" from tkinter import * 
top = Tk() 
top.geometry("200x150") 
top['bg']="#51E1DC" 
c = Canvas(top, bg="#51E1DC", height="200", width=200) 
#create arc 
arc = c.create_arc((50, 20, 150, 120), start=315, extent=270, fill="yellow") 
#create rectangle 
arc=c.create_rectangle((50, 120, 150, 140), fill="red") 
c.pack() 
top.mainloop()  """