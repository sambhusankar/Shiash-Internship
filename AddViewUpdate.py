from tkinter import *
import tkinter.messagebox
import mysql.connector

class EmployeeManagement:
    def __init__(self):
        self.root = Tk()
       
        self.db = mysql.connector.connect(user  = "root", password = "", host = "localhost", db = "employeemanagement")
        self.cursor =  self.db.cursor()
        self.root.geometry("700x600")
        self.root.title("Add View Update")
        self.root.configure(bg = "lightblue")
        self.ID = IntVar()
        self.Name = StringVar()
        self.Dept = StringVar()
        self.Dob = StringVar()
        self.Role = StringVar()
        self.Email  = StringVar()
        self.Phone = IntVar()
        self.EmpEditScreen()
        self.root.mainloop()
        

    def AddEmp(self):
        name = self.Name.get()
        dob = self.Dob.get()
        mail = self.Email.get()
        phone = self.Phone.get()
        role = self.Role.get()
        dept = self.Dept.get()
        if "@" in mail and name != "" and dob != "" and mail != "" and phone != "" and role != "" and dept != "":
            self.cursor.execute("insert into employees(Name, DOB, Email, Phone, Role, Dept) values(%s, %s, %s, %s, %s, %s)", [name, dob, mail, phone, role, dept])
            self.db.commit()
            tkinter.messagebox.showinfo("emp added", "Employee Added Successfully")
        else:
            tkinter.messagebox.showerror("emp addition err", "Please Enter Valid Details")
    
    def UpdateEmp(self):
        id = self.ID.get()
        name = self.Name.get()
        dept = self.Dept.get()
        dob = self.Dob.get()
        mail = self.Email.get()
        ph = self.Phone.get()
        role = self.Role.get()
        if id in self.Data.ID():
            self.cursor.execute("update employees set Name = %s, Dept = %s, DOB = %s, Email  = %s, Phone = %s, Role = %s where ID = %s", [name, dept, dob, mail, ph, role, id])
            self.db.commit()
            tkinter.messagebox.showinfo("update added", "Employee Updated Successfully")
        else:
            tkinter.messagebox.showerror("emp update err", "There is no Employee with this ID")

    def GoEmpEditPage(self):
        global activePage
        self.HomePage.pack_forget()
        self.EditPage.pack(fill = BOTH, expand = True)
        self.activePage = self.EditPage

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
        Label(self.root, text = "ID", bg = "lightblue", fg = "blue", font = ("calibri", 15)).place(x = 70, y = 100)
        Label(self.root, text = "Name", bg = "lightblue", fg = "blue", font = ("calibri", 15)).place(x = 70, y = 150)
        Label(self.root, text = "Department", bg = "lightblue", fg = "blue", font = ("calibri", 15)).place(x = 70, y = 200)
        Label(self.root, text = "DOB", bg = "lightblue", fg = "blue", font = ("calibri", 15)).place(x = 70, y = 250)
        Label(self.root, text = "Email", bg = "lightblue", fg = "blue", font = ("calibri", 15)).place(x = 70, y = 300)
        Label(self.root, text = "Phone", bg = "lightblue", fg = "blue", font = ("calibri", 15)).place(x = 70, y = 350)
        Label(self.root, text = "Role", bg = "lightblue", fg = "blue", font = ("calibri", 15)).place(x = 70, y = 400)

        Entry(self.root, textvariable = self.ID , bg = "lightblue", fg = "blue", font = ("calibri", 15)).place(x = 190, y = 100)
        Entry(self.root, textvariable = self.Name , bg = "lightblue", fg = "blue", font = ("calibri", 15)).place(x = 190, y = 150)
        Entry(self.root, textvariable = self.Dept , bg = "lightblue", fg = "blue", font = ("calibri", 15)).place(x = 190, y = 200)
        Entry(self.root, textvariable = self.Dob, bg = "lightblue", fg = "blue", font = ("calibri", 15)).place(x = 190, y = 250)
        Entry(self.root, textvariable = self.Email, bg = "lightblue", fg = "blue", font = ("calibri", 15)).place(x = 190, y = 300)
        Entry(self.root, textvariable = self.Phone, bg = "lightblue", fg = "blue", font = ("calibri", 15)).place(x = 190, y = 350)
        Entry(self.root, textvariable = self.Role, bg = "lightblue", fg = "blue", font = ("calibri", 15)).place(x = 190, y = 400)

        Button(self.root, text = "Add", bg = "blue", fg = "white", font = ("calibri", 15), command = self.AddEmp).place(x = 190, y = 450)
        Button(self.root, text = "Update", bg = "blue", fg = "white", font = ("calibri", 15), command = self.UpdateEmp).place(x = 290, y = 450)
        Button(self.root, text = "View", bg = "blue", fg = "white", font = ("calibri", 15), command = self.EmpView).place(x = 490, y = 450)


if __name__ == "__main__":
    E = EmployeeManagement()