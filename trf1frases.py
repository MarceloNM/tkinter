###############################################
# PI04 - António Marcelo Nicolau Marques
# 20240328
# Ex1 de Python avançado
# 


import tkinter as tk
import datetime
import time
import os
import re
import csv

#encoding: utf-8

def update_time():
    current_time = time.strftime("%H:%M:%S")
    lblhora.config(text = current_time)
    qdr.after(1000, update_time)
    
def terminar():         # fim do programa
    qdr.destroy()

def lerFrases(ficheiro):    # Carrega texto a partir de ficheiro (txt em formato csv) para lista
    global maxFrases
    existe = os.path.isfile(ficheiro)
    if existe:
        with open(ficheiro, mode = 'r', encoding="utf8") as fich:
            csvFile = csv.reader(fich)
            for linhas in csvFile:
                linhasp = []
                linhasp.append(linhas[0])
                linhasp.append(linhas[1])
#                linhasp.append(linhas[1].encode('utf-8'))
                Frases.append(linhasp)
        fich.close()
    maxFrases = len(Frases)

def mover(direcao):     # alteração da posição visível da lista 
    global posFrases
    global Frases
    global maxFrases
    global lingua
    if direcao == 0:
        if posFrases > 0:
            posFrases -= 1
        else:
            posFrases = maxFrases - 1 
    else:
        if posFrases < maxFrases - 1:
            posFrases += 1
        else: 
            posFrases = 0
    lblline.config(text = Frases[posFrases][lingua])  

def mudaLingua():       # alteração da posição na sub-lista  
    global posFrases
    global Frases
    global lingua
    if lingua == 0: 
        lingua = 1
        btnlingua.config(text = "English")
        btndown.config(text = "Seguinte")
        btnup.config(text = "Anterior")
        fechar.config(text ="Fechar")
    else: 
        lingua = 0
        btnlingua.config(text = "Portugues")
        btndown.config(text = "Next")
        btnup.config(text = "Previous")
        fechar.config(text ="Close")
    lblline.config(text = Frases[posFrases][lingua])


# main
Frases = []             # lista global com as frases 
maxFrases = 0           # variáveis globais de manipulação da lista
posFrases = 0
lingua = 0

path = 'Exemplos/'
# path = ''
ficheiro = path + 'frases.txt'

lerFrases(ficheiro)

qdr = tk.Tk()                   # definiçao da janela de trabalho
qdr.title("Pitão Zen")
qdr.configure(bg = "lightblue") # configuração da janela de trabalho
lblhora = tk.Label(qdr, bg = "lightblue", text = "hora bem")
lblhora.grid(row = 0, column = 0, padx = 10,)
update_time()
lblline = tk.Label(qdr, bg = "cyan", text = Frases[posFrases][0], width = 40, height = 3, wraplength= 250, font='helvetica 12')
lblline.grid(row = 3, column = 3, padx = 5, pady = 5)

# para passagem de parâmetros para métodos encontrei a 'variante' lambda...
btnup = tk.Button(qdr, bg = "yellow", text = "Previous", command = lambda : mover(0), width = 8)
btnup.grid(row = 2, column = 1, padx = 5, pady = 5)

btndown = tk.Button(qdr, bg = "orange", text = "Next", command = lambda : mover(1), width = 8)
btndown.grid(row = 2, column = 2, padx = 5, pady = 5)

# a mudança de língua muda a legenda do botão
btnlingua = tk.Button(qdr, bg = "blue", fg = "white", text = "Portugues", command = mudaLingua, width = 8)
btnlingua.grid(row = 4, column = 3, padx = 5, pady = 5)

fechar = tk.Button(qdr, bg = "lightgreen", text="Close", command = terminar, width = 8)
fechar.grid(row = 6, column = 0, padx = 5, pady = 5)


qdr.mainloop()



# fim do main


