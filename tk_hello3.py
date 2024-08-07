from tkinter import *
import tkinter as tk
import datetime
import time


def close_window():
    tk.destroy()

def update_time():
    current_time = time.strftime("%H:%M:%S")
    data = str(datetime.datetime.today())
    btn3.config(text = current_time)
    tk.after(1000, update_time)

tk = Tk()

btn1 = Label(tk, text = "Linha 0, Coluna 0")
btn1.grid(column = 0, row = 0, padx = 5, pady = 5)

btn2 = Label(tk, text = "Linha 0, Coluna 1")
btn2.grid(column = 1, row = 0, padx = 5, pady = 5)

btn3 = Label(tk, text = "Linha 1, Coluna 0")
btn3.grid(column = 0, row = 1, padx = 5, pady = 5)

btn4 = Label(tk, text = "Linha 1, Coluna 1")
btn4.grid(column = 1, row = 1, padx = 5, pady = 5)

btn5 = Label(tk, text = "Linha 2, Coluna 0")
btn5.grid(column = 0, row = 2, padx = 5, pady = 5)

btn6 = Label(tk, text = "Linha 2, Coluna 2")
btn6.grid(column = 2, row = 2, padx = 5, pady = 5)

btn7 = Label(tk, text = "Linha 2, Coluna 10")
btn7.grid(column = 10, row = 3, padx = 5, pady = 5)

Label(tk, text = "Linha 4, Coluna 3").grid(row = 4, column = 3, padx = 5, pady = 3)

label1 = Label(text = "u'll neva walkalone!", relief= RIDGE, width = 50).grid(row = 3)

close_button = Button(tk, text="Fechar", command = close_window, )
close_button.grid(column=3, row = 3, padx = 25, pady = 25)

update_time()

tk.mainloop()



