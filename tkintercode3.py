from tkinter import *

top=Tk()
top.title("main")
top.geometry('400x400')
def r():
    import tkintercode1
    top.destroy()

n1=Label(top,text="cust Name").grid(row=0,column=0)
e1=Entry(top).grid(row=0,column=1)


n3=Label(top,text="cust mail id").grid(row=1,column=0)
e3=Entry(top).grid(row=1,column=1)

n3=Label(top,text="custpassword").grid(row=2,column=0)
e3=Entry(top).grid(row=2,column=1)


n3=Label(top,text="cust contact number").grid(row=3,column=0)
e3=Entry(top).grid(row=3,column=1)

n3=Label(top,text="cust age").grid(row=4,column=0)
e3=Entry(top).grid(row=4,column=1)


n3=Label(top,text="opening account").grid(row=5,column=0)
e3=Entry(top).grid(row=5,column=1)

n3=Label(top,text="gender").grid(row=6,column=0)
e3=Entry(top).grid(row=6,column=1)

n3=Label(top,text="date of creation").grid(row=7,column=0)
e3=Entry(top).grid(row=7,column=1)


btn=Button(top,text="insert details").grid(row=8,column=0)
btn=Button(top,text="back to cust menu",command=r).grid(row=9,column=2)

