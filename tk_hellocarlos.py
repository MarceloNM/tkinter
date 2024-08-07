import tkinter as tk
import time

def update_time():
    current_time = time.strftime('%H:%M:%S')
    label2 = tk.Label(janela, text=current_time,bg="#E3Caa7",width=10,height=2,fg="white")
    label2.config(text=current_time)
    label2.grid(column=0,row=5)
    janela.after(1000, update_time)  #Atualiza a cada 1000 milisegundos (1 segundo)
def mudar_texto():
    label2.config(text="Verdadeiro")
# Função para sair
def close_window():
    janela.destroy()
# Criar uma janela
janela = tk.Tk()
janela.title("Olá turma PI04!")
janela.grid()

# Criar uma label
label = tk.Label(janela, text="Bem vindo ao Python em Janelas!",width=30)
label.grid(column=0,row=0,padx=5, pady=5)

label2 = tk.Label(janela, text="Dummy!",width=30)
label2.grid(column=0,row=1,padx=5, pady=5)
# Criar o botão para mostrar as horas
close_button = tk.Button(janela, text="HORAS", command= update_time, fg="#8A2BE2", bg="yellow", width=30)
close_button.grid(column=0,row=4,padx=5, pady=5)
# Criar o botão para mudar texto
mudar_button = tk.Button(janela, text="MUDAR", command= mudar_texto, fg="#8A2BE2", width=30)
mudar_button.grid(column=1,row=4,padx=5, pady=5)
# Criar o botão de fechar janela
close_button = tk.Button(janela, text="FECHAR", command= close_window, fg="red",width=30)
close_button.grid(column=1,row=5,padx=5, pady=5)

# Executar em loop
janela.mainloop()