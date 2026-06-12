# Exercício 
# Crie uma aplicação que pergunte o nome e o ano de nascimento do usuário
# Calcule a idade

import tkinter as tk
from tkinter import  messagebox, tkk







janela = tk.Tk()
janela.title("Cadastro de Usuário :)")
janela.geometry("500x400")
janela.configure (bg="white")

lbl_titulo = tk.Label(janela, text=("Arial", 14), fg="black", bg="white")
lbl_titulo.grid(row=0, column=0, pady=20, padx=20)

lbl_cadastro_usuario = tk.Label(janela, text="Digite o Seu Nome:", fg="black", bg="white")
lbl_cadastro_usuario.grid(row=1, column=0, pady=10, padx=20)

lbl_ano_usuario = tk.Label(janela, text="Digite Seu Ano de Nascimento:")
lbl_ano_usuario.grid(row=3, column=0, pady=10, padx=20)

ent_nome_usuario = tk.Entry(janela, font=("Ariual", 14), fg="black", bg="white")