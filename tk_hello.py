import tkinter as tk
import datetime
import time

from tkinter import messagebox

# from datetime import datetime


def update_time():
    current_time = time.strftime("%H:%M:%S")
    data = str(datetime.datetime.today())
    label3.config(text = current_time)
    janela.after(1000, update_time)
    
def close_window():
    janela.destroy()

# now = datetime.now()


# dataHoje = datetime.today()
# hora = time.hour()
#datahora = str(dataHoje) + " " + current_time
janela = tk.Tk()
janela.title("Bom dia interface gráfico")
label = tk.Label(janela, text = "Bem vindo ao Pitão arejado", width = 10)
label2 = tk.Label(janela, text = "Cuidado com as correntes de ar")
label3 = tk.Label(janela, text = "" )

label.pack(padx = 150, pady=10)
label2.pack(padx = 50, pady = 10)
label3.pack(padx = 50, pady = 10)

update_time()

dummy_button = tk.Button(janela, text = "Nada", command = "")
dummy_button.pack(padx = 20, pady = 20)

label4 = tk.Label(janela, text = "Dummy label")
label4.pack(padx = 20, pady = 20)

close_button = tk.Button(janela, text="Fechar", command = close_window)
close_button.pack(padx = 25, pady = 25)



janela.mainloop()

