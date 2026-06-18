# # tkinter 

# # componentens principais 
# # tk: a janela 
# # Label: Texto em rótulo 
# # Button: Um botão de clique
# # Entry: Um campo de entrada de texto 

# # Biblioteca 
# import tkinter as tk 
# from tkinter import messagebox

# # 1. Criar janela principal 
# janela = tk.Tk()
# janela.configure(bg="white")
# janela.title("Minha primeira jenela em GUI")
# janela.geometry("400x200") # Largura x Altura

# # 2. Criar a função que o botão vai executar (evento)
# def mostrar_mensagem():
#     messagebox.showinfo("Sucesso!", "Você clicou no botão! :)")

# # 3. Criar os componentes
# lbl_titulo = tk.Label(janela, text="Bem-Vindo à aula de Tkinter!", font=("Arial", 14, "bold"), bg="#ffffff")
# btn_clique = tk.Button(janela, text="Clique Aqui :) ", font=("Arial", 14), bg="#0C7FCC", fg="white", command=mostrar_mensagem)
                       
# # 4. Posicionar os Componentes
# lbl_titulo.pack(padx=20)
# btn_clique.pack(padx=10)
# # pady - posicionar vertical
# # padx - posicionar horizontal
# # 5. Rodar o loop da interface 
# janela.mainloop()

import tkinter as tk 
from tkinter import messagebox

# 1. Configurar evento 

def solicitar_informacoes():
    # .get() serve para buscar o texto que foi digitado
    nome_usuario = campo_nome.get()
    idade_usuario = int( campo_idade.get())
    if nome_usuario == "" and idade_usuario == "":
        messagebox.showwarning("Aviso", "Por Favor, digite seu nome :)")

    else:
        messagebox.showinfo("Saudações, querido aluno", f"Olá, {nome_usuario}, Sua idade é {2026-idade_usuario} Seja Bem-Vindo ao mundo das interfaces gráficas.")

# 2. Configuração de janela
app = tk.Tk()
app.title("Tela de Usuário")
app.geometry("300x300")

# 3. Componentes
lbl_nom_usuario = tk.Label(app, text="Digite Seu nome :) ").grid(row=0, column=0, padx=10, pady=10) # grid - posicionamento em grade


campo_nome = tk.Entry(app, font=("Arial", 12))
campo_nome.grid(row=1, column=0, padx=10, pady=5)

btn_cadastrar = tk.Button(app, text="Cadastrar",
command=solicitar_informacoes)
btn_cadastrar.grid(row=4, column=0, pady=15)

btn_fechar = tk.Button(app, text="Fechar", command=app.destroy)
btn_fechar.grid(row=5, column=0,pady=5)

lbl_idade_usuario = tk.Label(app,text="Digite o ano do seu nascimento:) ")
lbl_idade_usuario.grid(row=2, column=0, padx=10, pady=10)

campo_idade = tk.Entry(app,font=("Arial", 12))
campo_idade.grid(row=3, column=0, padx=10, pady=10)

btn_cadastrar = tk.Button(app, text="Cadastrar",
command=solicitar_informacoes)
# btn_cadastrar.pack(pady=15)

# 4. Rodar Interface
app.mainloop()
