
import tkinter as tk

from tkinter import *


def aviso():
    var = StringVar()
    aviso = Message(qdr, textvariable=var, relief=RAISED)
    var.set("Hey!? How are you doing?")
    #aviso.pack()


qdr = tk.Tk()
qdr.title("Lista de botões")

# from tkinter import *
# root = Tk()

# root.mainloop()
btn = []

#i = 1
for i in range(4):
    txt = "linha " + str(i) + " coluna " + str(i)
    #print(txt)
    bttnn = tk.Button(qdr, text = txt)
    bttnn.grid(column = i, row = i, padx = 50, pady = 5)
    #bttnn.pack(padx = 50, pady = 50)
    btn.append(bttnn)

msg = "ficheiro inexistente"

btn[2].config(text = Message(qdr, textvariable=msg, relief=RAISED))

qdr.mainloop()