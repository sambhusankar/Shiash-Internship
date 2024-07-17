from tkinter import *
import tkinter.messagebox
import mysql.connector

window = Tk()
window.geometry("700x700")
window.title("Product Details")
window.configure(bg = "lightblue")
db = mysql.connector.connect(host = "localhost", user = "root", password = "", db = "products")
cursor = db.cursor()
id = StringVar()
name = StringVar()
price = IntVar()
def Add():
    pr_id = id.get()
    pr_name = name.get()
    pr_price = price.get()
    cursor.execute("insert into details values(%s, %s, %s)", [pr_id, pr_name, pr_price])
    db.commit()
    tkinter.messagebox.showinfo("data added")
Entry(window, textvariable = id).place(x = 30, y = 30)
Entry(window, textvariable = name).place(x = 30, y = 60)
Entry(window, textvariable = price).place(x = 30, y = 90)
Button(window, text = "add", command = Add).place(x = 50, y = 120)

window.mainloop()