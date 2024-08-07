from tkinter import messagebox
import tkinter as tk
from tkinter.ttk import *
import os, csv


class Utilizador:
    def __init__(self, nome, pword): 
        self.nome = nome
        self.pword = pword

    def imprimirNome(self):
        print("Nome: " + self.nome)

    def imprimirPword(self):
        print("Pword: ", "***********")

def terminar():
    qdr.destroy()

def encript(palavra):
    epalavra = ''
    for i in palavra:
        epalavra += chr(ord(i)+3)
    print(epalavra)
    return epalavra

def userText(event):
    enterUN.delete(1,"end")

def lerUsers():
    print("Modo Read")       #############################################
    path = "Exemplos/users.csv"
    check_file = os.path.isfile(path)
    if (check_file):
        with open(path, mode = 'r') as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                print(lines)
                print(lines[0])
                Users.append(lines)
        file.close()
        for u in Users:
            print(u)
    else:
        print("Ficheiro ", path, " não existe!")
        
def appendUser(nome, pw):
    print("Modo write")
    path = "Exemplos/users.csv"
    check_file = os.path.isfile(path)
    if (check_file):
        with open(path, mode = 'w') as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                print(lines)
                print(lines[0])
                Users.append(lines)
        file.close()
        for u in Users:
            print(u)
    else:
        print("Ficheiro ", path, " não existe!")
    


def mostra():
    print("User name: %s Last Name: %s" % (enterUN.get(), enterPW.get()))
    

def regista():
    pw = encript(enterPW.get())
    nuser = -1
    for j in range(len(Users)):
        if Users[j][0] == enterUN.get(): nuser = j
    if nuser > -1:    # utilizador existe
        lblMsg.config(text = "Utilizador não registado")
    else:
        appendUser(enterUN.get(), pw)
    


def valida():
    # global Users
    pw = encript(enterPW.get())
    nuser = -1
    for j in range(len(Users)):
        if Users[j][0] == enterUN.get(): nuser = j
    if nuser > -1:    # utilizador existe
        if pw == Users[nuser][1]:
            lblMsg.config(text = "Logado")
        else:
            lblMsg.config(text = "Password errada")
    else:
        lblMsg.config(text = "Utilizador não registado")




Users = []

lerUsers()
# larg = input("largura:  ")
# altu = input("altura:  ")
# if (int(larg) < 300): larg = '300'
# if (int(altu) < 300): altu = '300'
z = "300" + "x" + "300"

qdr = tk.Tk()
qdr.wm_attributes("-topmost", 1)  # coloca a janela sobre as outras
qdr.geometry(z)

qdr.title("Login")
lbl1 = tk.Label(qdr, text = "Bem vindo ao Python Login")
lbl1.grid(row = 1, column=1, padx=25, pady=25)

lblUN = tk.Label(qdr, text="Utilizador")
lblUN.grid(row = 3, column = 1, padx=25,pady=25)

enterUN = tk.Entry(qdr, text = "User name")
enterUN.grid(row = 5, column = 1, padx=10, pady=10)

enterUN.insert(0,"Utilizador")
enterUN.bind("<FocusIn>", userText)

enterPW = tk.Entry(qdr, show="*", width=15, text = "Password")
enterPW.grid(row = 7, column = 1, padx=10, pady=10)

lblMsg = tk.Label(qdr, text = "        ", width= 20)
lblMsg.grid(row = 5, column = 2)

btnmostra = tk.Button(qdr, text = "Entrar", command = valida)
btnmostra.grid(row = 6, column = 2)

btnmostra = tk.Button(qdr, text = "Registar", command = regista)
btnmostra.grid(row = 7, column = 2)


fechar = tk.Button(qdr, bg = "grey", text="Close", command = terminar, width = 5, height=2)
fechar.grid(row = 9, column = 2, padx = 10, pady = 2)


qdr.mainloop()