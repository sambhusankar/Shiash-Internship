from tkinter import *
class ColorChange:
    def __init__(self):
        self.root = Tk()
    def Initializing(self):
        self.root.geometry("300x500")
        self.root.configure(bg  = "darkblue")
        def HandleClick(b):
            txt = b.cget("text")
            self.root.configure(bg = txt)
                
        B1 = Button(self.root, text = "red", bg = "red", command = lambda : HandleClick(B1))
        B1.place(x = 10, y = 20)
        B2 = Button(self.root, text = "green", bg = "Green", command = lambda : HandleClick(B2))
        B2.place(x = 60, y = 20)
        B3 = Button(self.root, text = "blue", bg = "Blue", command = lambda : HandleClick(B3))
        B3.place(x = 120, y = 20)
        Can = Canvas(self.root, height = 150, width = 150, bg = "white")
        Can.place(x = 10, y = 150)
        triangle_points = [20, 130, 80, 130, 50, 180]
        Can.create_polygon(triangle_points, fill = "black", width = 2)
        self.root.mainloop()
if __name__ == "__main__":
    C =  ColorChange()
    C.Initializing()