from tkinter import *
from tkinter import messagebox
obj = Tk()
obj.geometry("300x300")
obj.title("calculator")
obj.configure(bg = "aqua")
Label(obj, text = "Enter number 1", bg = "aqua", fg = "black").place(x = 30, y = 30)
Label(obj, text = "Enter number 1", bg = "aqua", fg = "black").place(x = 30, y = 60)
num1 = IntVar()
num2 = IntVar()
result = IntVar()
def Add():
    result.set(num1.get() + num2.get())
def Sub():
    result.set(num1.get() - num2.get())
def Mul():
    result.set(num1.get() * num2.get())
def Div():
    try:
        result.set(num1.get() / num2.get())
    except ZeroDivisionError as e:
        print(e)
    
Entry(obj, textvariable = num1).place(x = 120, y = 30)
Entry(obj, textvariable = num2).place(x = 120, y = 60)
Button(obj, text = "+", bg = "white", command = Add).place(x = 60, y = 110)
Button(obj, text = "-", bg = "white", command = Sub).place(x = 120, y = 110)
Button(obj, text = "x", bg = "white", command = Mul).place(x = 180, y = 110)
Button(obj, text = "÷", bg = "white", command = Div).place(x = 240, y = 110)
Label(obj, text = "result").place(x =  50, y = 170)
Entry(obj, textvariable = result, fg = "red",bg = "aqua").place(x = 100, y= 170)
obj.mainloop()