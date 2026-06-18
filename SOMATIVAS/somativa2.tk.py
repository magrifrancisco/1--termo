# 1- Registro de Operador: Peça o nome do operador e o turno (A, B ou C). Exiba:
# "Operador [Nome] registrado no Turno [Turno]. Boa jornada!"




# import tkinter as tk 
# from tkinter import messagebox, ttk

# def cadastro_operador ():
#     nome_operador = ent_nome_operador.get()
#     opcao_turno = cmb_turno.get()

#     if nome_operador == "" and opcao_turno == "":
#         messagebox.showwarning("Verficar Dados", "Verificar os Campos")
#     else:
#         messagebox.showinfo("Boa Jornanda :)", f"Olá usuário {nome_operador}, Seu Turno é: {opcao_turno}")


# janela = tk.Tk()
# janela.title("Cadastro de Operador :)")
# janela.geometry("500x400")
# janela.configure (bg="white")

# lbl_titulo = tk.Label(janela, text="Cadastro De Operador", font=("Arial", 14), fg="black", bg="white")
# lbl_titulo.grid(row=0, column=0, pady=20, padx=20)


# lbl_nome_operador = tk.Label(janela, text="Digite Seu Nome", font=("Arial", 14), fg="black", bg="white")
# lbl_nome_operador.grid(row=1, column=0, pady=20, padx=20)

# ent_nome_operador = tk.Entry(janela, font=("Arial", 14), fg="black", bg="white")
# ent_nome_operador.grid(row=2, column=0, pady=20, padx=10)

# lbl_turno = tk.Label(janela, text="Escolha Seu Turno",font=("Arial", 14), fg="black",bg="white")
# lbl_turno.grid(row=3, column=0, pady=20, padx=20)


# cmb_turno = ttk.Combobox(janela, values=["Turno A", "Turno B", "Turno C"])
# cmb_turno.grid(row=4, column=0, pady=20, padx=20)


# btn_enviar = tk.Button(janela, text="Entrar", bg="green", fg="white",width=7,height=3, command=cadastro_operador)
# btn_enviar.grid(row=5, column=0, pady=10, padx=10)

# janela.mainloop()


# 2- Cálculo de Produção: Peça a quantidade de peças produzidas em 1 hora. Calcule e
# exiba quantas peças serão produzidas em um turno de 8 horas.


# import tkinter as tk
# from tkinter import messagebox


# def calcular_producao():
#     if ent_quantidade_pecas.get() == "":
#         messagebox.showwarning("Verificar Dados", "insira a quantidade de peças produzidas em 1 hora.")
#     elif ent_quantidade_pecas.get():
#         quantidade_pecas = int(ent_quantidade_pecas.get())
#         producao_turno = quantidade_pecas * 8
#         messagebox.showinfo("Produção Total", f"Em um turno de 8 horas, serão produzidas {producao_turno} peças.")
#     else:
#         messagebox.showerror("Erro", "Por favor, insira um número válido.")


# janela = tk.Tk()
# janela.title("Cálculo de Produção")
# janela.geometry("400x300")
# janela.configure(bg="white")
# lbl_quantidade_pecas = tk.Label(janela, text="Quantidade de peças produzidas em 1 hora:")
# lbl_quantidade_pecas.pack(pady=10)
# ent_quantidade_pecas = tk.Entry(janela)
# ent_quantidade_pecas.pack(pady=5)
# btn_calcular = tk.Button(janela, text="Calcular Produção", command=calcular_producao)
# btn_calcular.pack(pady=10)

# janela.mainloop()


# 3- Conversor de Unidade: O sistema lê uma pressão em Bar. Converta para PSI (1 Bar
# ≈ 14.5 PSI) e exiba com duas casas decimais.

# import tkinter as tk
# from tkinter import messagebox

# def converter_pressao():
#     if ent_pressao_bar.get() == "":
#         messagebox.showwarning("Verificar Dados", "Insira a pressão em Bar.")
#     elif ent_pressao_bar.get():
#         pressao_bar = float(ent_pressao_bar.get())
#         pressao_psi = pressao_bar * 14.5
#         messagebox.showinfo("Pressão Convertida", f"{pressao_bar:.2f} Bar é equivalente a {pressao_psi:.2f} PSI.")
#     else:
#         messagebox.showerror("Erro", "Por favor, insira um número válido.")

# janela = tk.Tk()
# janela.title("Conversor de Pressão")
# janela.geometry("400x300")
# janela.configure(bg="white")
# lbl_pressao_bar = tk.Label(janela, text="Pressão em Bar:")
# lbl_pressao_bar.pack(pady=10)
# ent_pressao_bar = tk.Entry(janela)
# ent_pressao_bar.pack(pady=5)
# btn_converter = tk.Button(janela, text="Converter para PSI", command=converter_pressao)
# btn_converter.pack(pady=10)
# janela.mainloop()


# 4 - Média de Qualidade: Peça 3 notas de inspeção de uma peça (0 a 10). Exiba a média
# aritmética simples delas.

# import tkinter as tk
# from tkinter import messagebox, ttk

# def calcular_media():
#     if ent_caixa_1.get() == "" or ent_caixa_2.get() == "" or ent_caixa_3.get() == "":
#         messagebox.showwarning("Verificar Dados", "Preencha todas as notas de inspeção.")
#     if not (ent_caixa_1.get() and ent_caixa_2.get() and ent_caixa_3.get()):
#         messagebox.showerror("Erro", "Por favor, insira números válidos para as notas.")                

#     if ent_caixa_1.get() and ent_caixa_2.get() and ent_caixa_3.get():
#         if ent_caixa_1.get == "" or ent_caixa_2.get() == "" or ent_caixa_3.get() == "":
#             messagebox.showerror("Erro", "As notas devem estar entre 0 e 10.")
#     nota1 = float(ent_caixa_1.get())
#     nota2 = float(ent_caixa_2.get())
#     nota3 = float(ent_caixa_3.get())
#     media = (nota1 + nota2 + nota3) / 3
#     messagebox.showinfo("Média de Qualidade", f"A média aritmética das notas é: {media:.2f}")
    
# messagebox.showerror("Erro", "Por favor, insira números válidos para as notas.")



# janela = tk.Tk()
# janela.title("Média de Qualidade :)")
# janela.geometry("500x400")
# janela.configure (bg="lightblue")

# lbl_titulo = tk.Label(janela, text=("Média de Qualidade"), font=("Arial", 14), fg="black", bg="lightblue",)
# lbl_titulo.grid(row=0, column=0, pady=20, padx=20)

# lbl_caixa_1 = tk.Label(janela, text="Nota 1", font=("Arial", 14), fg="black", bg="lightblue")
# lbl_caixa_1.grid(row=1, column=0, pady=20, padx=20)

# ent_caixa_1 = tk.Entry(janela, font=("Arial", 14), fg="black", bg="lightblue")
# ent_caixa_1.grid(row=2, column=1, pady=20, padx=10)

# lbl_caixa_2 = tk.Label(janela, text="Nota2", font=("Arial", 14), fg="black", bg="lightblue")
# lbl_caixa_2.grid(row=3, column=0, pady=20, padx=20)

# ent_caixa_2 = tk.Entry(janela, font= ("Arial", 14), fg="black", bg="lightblue")
# ent_caixa_2.grid(row=3, column=1, pady=20, padx=10)

# lbl_caixa_3 = tk.Label(janela, text="Nota3", font=("Arial", 14), fg="black", bg="lightblue",)
# lbl_caixa_3.grid(row=4, column=0, pady=20, padx=20)

# ent_caixa_3 = tk.Entry(janela, font=("Arial", 14), fg="black", bg="lightblue")
# ent_caixa_3.grid(row=4, column=1, pady=20, padx=10)


# 5 - Termostato Inteligente: Peça a temperatura de um motor.
# ● Abaixo de 40°C: "Baixa carga".
# ● Entre 40°C e 70°C: "Normal".
# ● Acima de 70°C: "ALERTA: Resfriamento Ativado!".

# import tkinter as tk
# from tkinter import messagebox, ttk
# def verificar_temperatura():
#     if ent_temperatura_motor.get() == "":
#         messagebox.showwarning("Verificar Dados", "Insira a temperatura do motor.")
#     elif ent_temperatura_motor.get():
#         temperatura = float(ent_temperatura_motor.get())
#         if temperatura < 40:
#             messagebox.showinfo("Status do Motor", "Baixa carga")
#         elif 40 <= temperatura <= 70:
#             messagebox.showinfo("Status do Motor", "Normal")
#         else:
#             messagebox.showwarning("ALERTA", "ALERTA: Resfriamento Ativado!")
#     else:
#         messagebox.showerror("Erro", "Por favor, insira um número válido.")

# janela = tk.Tk()
# janela.title("Termostato Inteligente")
# janela.geometry("400x300")
# janela.configure(bg="white")

# lbl_temperatura_motor = tk.Label(janela, text="Temperatura do Motor (°C):")
# lbl_temperatura_motor.grid(row=0, column=0, pady=10, padx=10)

# ent_temperatura_motor = tk.Entry(janela)
# ent_temperatura_motor.grid(row=0, column=1, pady=5)

# btn_verificar = tk.Button(janela, text="Verificar Temperatura", command=verificar_temperatura)
# btn_verificar.grid(row=1, column=0, columnspan=2, pady=10)

# janela.mainloop()

# 6. Classificador de Lotes: O usuário insere o código do produto. Se começar com "A",
# exiba "Alimentos". Se "E", "Eletrônicos". Para qualquer outro, "Desconhecido".

# import tkinter as tk
# from tkinter import messagebox, ttk

# def classificar_lote():
#     codigo_produto = ent_codigo_produto.get()
#     if codigo_produto == "":
#         messagebox.showwarning("Verificar Dados", "Insira o código do produto.")
#     elif codigo_produto.startswith("A"):
#         messagebox.showinfo("Classificação do Lote", "Alimentos")
#     elif codigo_produto.startswith("E"):
#         messagebox.showinfo("Classificação do Lote", "Eletrônicos")
#     else:
#         messagebox.showinfo("Classificação do Lote", "Desconecido")

# janela = tk.Tk()
# janela.title("Classificador de Lotes")
# janela.geometry("400x300")
# janela.configure(bg="white")

# lbl_codigo_produto = tk.Label(janela, text="Código do Produto:")
# lbl_codigo_produto.grid(row=0, column=0, pady=10, padx=10)

# ent_codigo_produto = tk.Entry(janela)
# ent_codigo_produto.grid(row=0, column=1, pady=5)

# btn_classificar = tk.Button(janela, text="Classificar Lote", bg="green", command=classificar_lote)
# btn_classificar.grid(row=1, column=0, columnspan=2, pady=10)

# janela.mainloop()

# 7- Segurança de Operação: A máquina só liga se o sensor_porta == "fechada" E o
# botao_emergencia == "desligado". Peça esses dois inputs e diga se a máquina pode
# iniciar.

# import tkinter as tk
# from tkinter import messagebox, ttk
# def verificar_seguranca():
#     sensor_porta = cmb_sensor_porta.get()
#     botao_emergencia = cmb_botao_emergencia.get()

#     if sensor_porta == "fechada" and botao_emergencia == "desligado":
#         messagebox.showinfo("Segurança de Operação", "A máquina pode iniciar.")
#     else:
#         messagebox.showwarning("Segurança de Operação", "A máquina NÃO pode iniciar. Verifique os sensores.")
    
# janela = tk.Tk()
# janela.title("Segurança de Operação")
# janela.geometry("400x300")
# janela.configure(bg="white")

# lbl_sensor_porta = tk.Label(janela, text="Sensor da Porta:")
# lbl_sensor_porta.grid(row=0, column=0, pady=10, padx=10)

# cmb_sensor_porta = ttk.Combobox(janela, values=["fechada", "aberta"])
# cmb_sensor_porta.grid(row=0, column=1, pady=5)

# lbl_botao_emergencia = tk.Label(janela, text="Botão de Emergência:")
# lbl_botao_emergencia.grid(row=1, column=0, pady=10, padx=10)

# cmb_botao_emergencia = ttk.Combobox(janela, values=["desligado", "ligado"])
# cmb_botao_emergencia.grid(row=1, column=1, pady=5)

# btn_verificar = tk.Button(janela, text="Verificar Segurança", bg="green", command=verificar_seguranca)
# btn_verificar.grid(row=2, column=0, columnspan=2, pady=10)

# janela.mainloop()
