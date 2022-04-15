import tkinter
from tkinter import *
from tkinter import ttk
from binary import main as B
from sidewiner import main as S
from DFS import main as D
from DFS import main2 as D2
from wilson import main as W


root = Tk()

label1 = tkinter.Label(root,text="MAZE GENERATOR")
label1.grid(row=0,column=0)

label2=tkinter.Label(root,text="CHOOSE ALGORITHM")
label2.grid(row=1,column=0)


variable = StringVar(root)
option = OptionMenu(root, variable, "DFS", "DFS_SOLVER", "Binary Tree", "Side Winer","Wilson")
option.grid(row=1,column=1)

label3=tkinter.Label(root,text="")
label3.grid(row=4,column=1,padx=10,pady=10)
label4=tkinter.Label(root,text="TIME OF GENERATING:")
label4.grid(row=4,column=0,padx=10,pady=10)
label5=tkinter.Label(root,text="TIME OF SOLVING:")
label5.grid(row=5, column=0, padx=10, pady=10)
label6=tkinter.Label(root,text="")
label6.grid(row=5, column=1, padx=10, pady=10)
def Run():
    if variable.get()=="DFS":
        time =float(round(D(),3))
        label3.config(text=time)
        label5.grid_forget()
        label6.grid_forget()
    if variable.get()=="Binary Tree":
        time=float(round(B(),3))
        label3.config(text=time)
        label5.grid_forget()
        label6.grid_forget()
    if variable.get()=="Side Winer":
        time=float(round(S(),3))
        label3.config(text=time)
        label5.grid_forget()
        label6.grid_forget()
    if variable.get()=="Wilson":
        time=float(round(W(),3))
        label3.config(text=time)
        label5.grid_forget()
        label6.grid_forget()
    if variable.get()=="DFS_SOLVER":
        time = float(round(D2(), 3))
        label6.config(text=time)

button1=tkinter.Button(text="RUN",bg="red",command=Run)
button1.grid(row=2,column=0,padx=10,pady=10)
root.mainloop()