from tkinter import *
import tkinter.messagebox
import mysql.connector
from tkcalendar import DateEntry
from  ..Store import data

class EmployeeEdit:
    def __init__(self):
        self.root = Tk()
        self.db = mysql.connector.connect(user  = "root", password = "", host = "localhost", db = "employeemanagement")
        self.cursor =  self.db.cursor()
        self.root.geometry("700x600")
        self.root.title("Employee Management System")
        self.root.configure(bg = "lightblue")
        self.ID = IntVar()
        self.Name = StringVar()
        self.Dept = StringVar()
        self.Dob = StringVar()
        self.Role = StringVar()
        self.Email  = StringVar()
        self.Phone = IntVar()
        self.EditPage = Frame(self.root, bg = "lightblue")
        self.activePage = None
        self.EmpEditScreen()
        self.root.mainloop()

    def AddEmp(self):
        name =  self.Name.get()
        dob = self.Dob.get()
        mail = self.Email.get()
        phone = self.Phone.get()
        role = self.Role.get()
        dept = self.Dept.get()
        self.cursor.execute("insert into employees(Name, DOB, Email, Phone, Role, Dept) values(%s, %s, %s, %s, %s, %s)", [name, dob, mail, phone, role, dept])
        self.db.commit()
    
    def UpdateEmp(self):
        id = self.ID.get()
        name = self.Name.get()
        dept = self.Dept.get()
        dob = self.Dob.get()
        mail = self.Email.get()
        ph = self.Phone.get()
        role = self.Role.get()
        self.cursor.execute("update employees set Name = %s, Dept = %s, DOB = %s, Email  = %s, Phone = %s, Role = %s where ID = %s", [name, dept, dob, mail, ph, role, id])
        self.db.commit()

    def Back(self):
        self.activePage.pack_forget()
        self.HomePage.pack(fill = BOTH, expand = True)

    def GoEmpEditPage(self):
        global activePage
        self.HomePage.pack_forget()
        self.EditPage.pack(fill = BOTH, expand = True)
        self.activePage = self.EditPage

    def EmpDelete(self):
        id = self.ID.get()
        self.cursor.execute("delete from employees where Id = %s", [id])
        self.db.commit()

    def EmpView(self):
        id = self.ID.get()
        self.cursor.execute("select * from employees where Id = %s", [id])
        data = self.cursor.fetchall()
        if len(data)  > 0:
            self.Name.set(data[0][1])
            self.Dob.set(data[0][2])
            self.Email.set(data[0][3])
            self.Phone.set(data[0][4])
            self.Role.set(data[0][5])
            self.Dept.set(data[0][6])
        else:
            tkinter.messagebox.showerror("no data", "There is no user with this ID")

    def EmpEditScreen(self):
        Label(self.EditPage, text = "ID", bg = "lightblue", fg = "blue", font = ("calibri", 15)).place(x = 70, y = 100)
        Label(self.EditPage, text = "Name", bg = "lightblue", fg = "blue", font = ("calibri", 15)).place(x = 70, y = 150)
        Label(self.EditPage, text = "Department", bg = "lightblue", fg = "blue", font = ("calibri", 15)).place(x = 70, y = 200)
        Label(self.EditPage, text = "DOB", bg = "lightblue", fg = "blue", font = ("calibri", 15)).place(x = 70, y = 250)
        Label(self.EditPage, text = "Email", bg = "lightblue", fg = "blue", font = ("calibri", 15)).place(x = 70, y = 300)
        Label(self.EditPage, text = "Phone", bg = "lightblue", fg = "blue", font = ("calibri", 15)).place(x = 70, y = 350)
        Label(self.EditPage, text = "Role", bg = "lightblue", fg = "blue", font = ("calibri", 15)).place(x = 70, y = 400)

        Entry(self.EditPage, textvariable = self.ID , bg = "lightblue", fg = "blue", font = ("calibri", 15)).place(x = 190, y = 100)
        Entry(self.EditPage, textvariable = self.Name , bg = "lightblue", fg = "blue", font = ("calibri", 15)).place(x = 190, y = 150)
        Entry(self.EditPage, textvariable = self.Dept , bg = "lightblue", fg = "blue", font = ("calibri", 15)).place(x = 190, y = 200)
        DateEntry(self.EditPage, textvariable = self.Dob, bg = "lightblue", fg = "blue", font = ("calibri", 15)).place(x = 190, y = 250)
        Entry(self.EditPage, textvariable = self.Email, bg = "lightblue", fg = "blue", font = ("calibri", 15)).place(x = 190, y = 300)
        Entry(self.EditPage, textvariable = self.Phone, bg = "lightblue", fg = "blue", font = ("calibri", 15)).place(x = 190, y = 350)
        Entry(self.EditPage, textvariable = self.Role, bg = "lightblue", fg = "blue", font = ("calibri", 15)).place(x = 190, y = 400)

        Button(self.EditPage, text = "Add", bg = "blue", fg = "white", font = ("calibri", 15), command = self.AddEmp).place(x = 190, y = 450)
        Button(self.EditPage, text = "Update", bg = "blue", fg = "white", font = ("calibri", 15), command = self.UpdateEmp).place(x = 290, y = 450)
        Button(self.EditPage, text = "Delete", bg = "blue", fg = "white", font = ("calibri", 15), command = self.EmpDelete).place(x = 390, y = 450)
        Button(self.EditPage, text = "View", bg = "blue", fg = "white", font = ("calibri", 15), command = self.EmpView).place(x = 490, y = 450)

        Button(self.EditPage, text = "Back", bg = "blue", fg = "white", font = ("calibri", 15), command = self.Back).place(x = 10, y = 10)

  
if __name__ == "__main__":
    E = EmployeeEdit()