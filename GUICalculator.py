from tkinter import *

window = Tk()
window.geometry('300x500')
window.title("Sankar's Calculator")
window.configure(bg = "black")

#just creating two frames for buttons and results
results = Frame(window,  height = 150, width = 300, bg = "#121A27")
buttons = Frame(window, bg = "#111B26")
results.place(x = 0, y = 0)
buttons.place(x = 0, y = 150, height = 350, width = 300)
#results
calcs = StringVar()
actual = StringVar()
Label(results, text = "Sakar's Calculator", fg = "white",bg = "#121A27", font = ("arial", 15)).place(x = 0, y = 0)
Entry(results, textvariable = calcs, font = ("arial", 15), bg = "#121A27", fg = "white", justify =  RIGHT).place(x = 0, y = 50, height = 50, width = 300)
Entry(results,textvariable = actual, font = ("arial", 25), bg = "#121A27", fg = "white", justify =  RIGHT).place(x = 0, y = 100, height = 50, width = 300)

#button click event handling
def Click(b):
    btn_txt = b.cget("text")
    calcs_txt = calcs.get()
    if(btn_txt not in ["C", "=", "⌫"]):
        if len(calcs_txt) == 0 and btn_txt not in ["+", "/", "*", "%"]: #preventing operatror to be the first
            current = calcs.get()
            calcs.set(current + btn_txt)
        if len(calcs_txt) >= 1:
            if calcs_txt[-1] in ["-", "+", "/", "*", "%"] and btn_txt in ["-", "+", "/", "*", "%"]: #checking for operator collison
                pass
            else:
                current = calcs.get()
                calcs.set(current + btn_txt)
                try:
                    actual.set(eval(calcs.get()))
                except Exception as e:
                    print(e)
    elif(btn_txt == "C"):
        calcs.set("")
        actual.set("")
    elif(btn_txt == "⌫"):
        current = calcs.get()
        if(len(current) >= 1):
            calcs.set(current[:-1])
            try:
                actual.set(eval(calcs.get()))
            except Exception as e:
                print(e)
        else:
            actual.set("")
    elif(btn_txt == "="):
        try:
            actual.set(eval(calcs.get()))
        except Exception as e:
            print(e)

#setting up the colors to buttons 
def SetColors():
    for btn in  buttons.winfo_children():
        if btn.cget("text") in ["C", "*", "/", "-", "+", "%", "⌫"]:
            btn.configure(bg = "#1B67A5")
        if btn.cget("text") == "=":
            btn.configure(bg = "#9EBE74",fg = "black")

#buttons 
btn_txt = ["C", "%", "⌫", "/", "7", "8", "9", "*", "4", "5", "6", "-", "1", "2", "3", "+", "00", "0", ".", "="]
index = 0
for i in range(5):
    for j in range(4): 
        btn = Button(buttons, text = btn_txt[index], bg = "#273E53", height = 2, width = 5, font = ("arial", 15), fg = "white")
        btn.grid(row = i, column = j, padx = 5, pady = 2.5)
        btn.config(command = lambda b = btn: Click(b))
        index += 1
SetColors()
        
window.mainloop()