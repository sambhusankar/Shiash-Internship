from tkinter import *
import tkinter.messagebox
class Game:
    def __init__(self):
        self.root = Tk()
        self.root.title("Tic-Tac-Toe")
        self.root.geometry("500x500")
        self.root.configure(bg = "#2b1640")
        self.plr1 = StringVar()
        self.plr2 = StringVar()
        self.CreateNames()
        self.CreateGameBoard()
        self.Reset()
        self.move = 0
        self.CheckDraw()
        self.X = True
        self.O = False
        self.win =  False
        self.root.mainloop()

    def CreateNames(self):
        Label(self.root,  text = "Tic-Tac-Toe by Sankar", fg = "#cffcfc", font =  ("arial", 20), bg = "#2b1640").place(x = 100,  y = 5)
        Label(self.root, text = "Player1").place(x = 50, y =  44)
        Label(self.root, text = "Player2").place(x = 50, y =  94)
        Entry(self.root, textvariable =  self.plr1, font = ("arial", 20), fg = "white", bg = "#2b1640").place(x = 100, y = 40)
        Entry(self.root, textvariable =  self.plr2, font = ("arial", 20), fg = "white", bg = "#2b1640").place(x = 100, y = 90)
        Button(self.root, text =  "↻", fg = "white",bg = "blue", height = 3, width = 7, command = self.Reset).place(x = 410, y = 20)

    def CheckWin(self):
        
        wins = [
            [B1["text"], B2["text"], B3["text"]],
            [B4["text"], B5["text"], B6["text"]],
            [B7["text"], B8["text"], B9["text"]],
            [B1["text"], B4["text"], B7["text"]],
            [B2["text"], B5["text"], B8["text"]],
            [B3["text"], B6["text"], B9["text"]],
            [B1["text"], B5["text"], B9["text"]],
            [B3["text"], B5["text"], B7["text"]]
        ]
        for i in range(len((wins))):
            if self.win == False:
                if wins[i][0] == "X" and wins[i][1] == "X" and wins[i][2] == "X":
                    tkinter.messagebox.showinfo("win",f"{self.plr1.get()} win")
                    self.win = True
                    
                if wins[i][0] == "O" and wins[i][1] == "O" and wins[i][2] == "O":
                    tkinter.messagebox.showinfo("Win", f"{self.plr2.get()} win")
                    self.win = True
                    

    def CheckDraw(self):
        if  self.move == 9 and self.win == False:
            tkinter.messagebox.showwarning("draw",  "match draw")

    def HandleClick(self, btn):
        if self.plr1.get() != "" and self.plr2.get() != "":
            if self.win == False:
                if self.X == True and btn["text"] ==  "":
                    btn.configure(text = "X")
                    self.X = False
                    self.O = True
                    self.move += 1
                elif self.O == True and btn["text"] ==  "":
                    btn.configure(text = "O")
                    self.X = True
                    self.O = False
                    self.move += 1
                self.CheckWin()
                self.CheckDraw()
        else:
            tkinter.messagebox.showerror("user", "Please eneter your name")
    def CreateGameBoard(self):
        global B1, B2, B3, B4, B5, B6, B7, B8, B9
        B1 = Button(self.root, text = "", height = 2, width = 5, font = ("arial", 20), command = lambda : self.HandleClick(B1))
        B1.place(x = 100, y = 200)
        B2 = Button(self.root, text = "", height = 2, width = 5, font = ("arial", 20), command = lambda : self.HandleClick(B2))
        B2.place(x =200, y = 200)
        B3 = Button(self.root, text = "", height = 2, width = 5, font = ("arial", 20), command = lambda : self.HandleClick(B3))
        B3.place(x = 300, y = 200)
        
        B4 = Button(self.root, text = "", height = 2, width = 5, font = ("arial", 20), command = lambda : self.HandleClick(B4))
        B4.place(x = 100, y = 300)
        B5 = Button(self.root, text = "", height = 2, width = 5, font = ("arial", 20), command = lambda : self.HandleClick(B5))
        B5.place(x =200, y = 300)
        B6 = Button(self.root, text = "", height = 2, width = 5, font = ("arial", 20), command = lambda : self.HandleClick(B6))
        B6.place(x = 300, y = 300)
        
        B7 = Button(self.root, text = "", height = 2, width = 5, font = ("arial", 20), command = lambda : self.HandleClick(B7))
        B7.place(x = 100, y = 400)
        B8 = Button(self.root, text = "", height = 2, width = 5, font = ("arial", 20), command = lambda : self.HandleClick(B8))
        B8.place(x =200, y = 400)
        B9 = Button(self.root, text = "", height = 2, width = 5, font = ("arial", 20), command = lambda : self.HandleClick(B9))
        B9.place(x = 300, y = 400)
        
    def Reset(self):
        self.plr1.set("")
        self.plr2.set("")
        B1['text'] = B2['text'] = B3['text'] = B4['text'] = B5['text'] = B6['text'] = B7['text'] = B8['text'] = B9['text'] = ""
        self.win = False
        self.move = 0

if __name__ == "__main__":
    G = Game()
    