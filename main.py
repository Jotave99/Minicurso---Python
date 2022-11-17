from tkinter import Tk, Label, messagebox
import tkinter as tk
from tkinter.ttk import Entry, Button

root = Tk()
root.title("Desv Python")
root.geometry("950x600")
root.configure(background="#1e1e1e")

Titulo = Label(root, text="Olá, mundo!", bg="#1e1e1e", foreground="white", font=('Century Gothic', 20))
Titulo.pack()

nomeLabel = Label(root, text="Nome:", bg="#1e1e1e", foreground="white", font=('Century Gothic', 18))
nomeLabel.pack()

nomeEntry = Entry(root)
nomeEntry.pack()

def pegaNome():
    nome = nomeEntry.get()
    messagebox.showinfo(title="info", message=nome)


pegaNomeButton = Button(root, text="Pega nome", command=pegaNome)
pegaNomeButton.pack()

root.mainloop()