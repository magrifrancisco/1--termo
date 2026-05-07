# idade = input("Digite a sua idade:")
# if idade >= 18:
#     print("Você é maior de idade.")

#Corrigido 

# idade = float (input("Digite a sua idade"))
# if idade >= 18:
#     print("Você é maior de idade")
# elif idade <=18:
#     print("Você é menor de idade")

# 2. A escrita fiel
# nome = "Mariana"
# print("Seja bem-vinda, nome!")

# corrigido

# nome = "Mariana"
# print("Seja Bem-Vinda", nome)


# 3. Falta de Espaço
# numero = 10
# if numero >5:
#     print("O número é maior que cinco")
# else:
#     print("O número é menor ou igual a cinco.")

# corrigido

# numero = float(input("Qual é o número?"))
# if numero >= 5:
#     print("O número é maior ou igual a cinco?")
# else:
#     print("O número é menor ou igual a cinco.")


# 4. Esquecimento Fatal 
# usuario = "aluno123"
# if usuario == "aluno123"
#     print("Login realizado com sucesso.")

# corrigido

# usuario = input("Digite o seu nome de usuário.")
# if usuario == "aluno123":
#     print("Login realizado com sucesso!")
# else:
#     print("Não foi possível realizar o login:(")


# 5. Atribuição vs. Comparação
# clima = "ensolarado"
# if clima = "chuvoso":
    # print("Leve um guarda-chuva!")

# Corrigido  

# clima = input("Como está o clima hoje?:")
# if clima == "chuvoso":
#     print("Leve um guarda-chuva ☂")
# elif clima == "ensolarado":
#     print("Pode ir tranquilo, está ensolarado ☀")


# Misturando Alhos com Bugalhos
# pontos = 50
# print("Parabéns! Você fez"+ pontos "+ pontos")

# Corrigido

# pontos = "+50 pontos"
# print("parabéns! Você fez", pontos)


# 7. A Ordem dos Fatores
# O Sistema deve dar "Excelente" para notas 9 ou 10.
# nota = 9.5
# if nota >=7:
#     print("Aprovado")
# elif nota >=9:
#     print("Excelente! ")

# Corrigido 

# nota = float(input("Qual é a usa nota?:"))
# if nota == 7:
#     print("Aprovado 👍")
# elif nota == 8:
#      print("Aprovado 👍")
# elif nota  >=9:
#     print("Excelente 😁")


# 8. O Contador de 1 a 5
# Objetivo: Mostrar na tela os números 1, 2, 3, 4 e 5.
# for i in range(5):
# print(i)

# Corrigido 

# for i in range (1, 6):
#     print(i)


# 9. O Loop Eterno
# tentativas = 1
# while tentativas <= 3:
# print("Tentando conectar...")
# O código deveria parar após 3 tentativas

# Corrigido

# tentativas = 1
# while tentativas <=3:
#     print("tentando conectar...")
#     tentativas = tentativas +1


# 10. A Senha Teimosa
# O programa deve pedir a senha até que o usuário digite "python123"
# senha = ""
# while senha == "python123":
# senha = input("Digite a senha secreta: ")
# print("Acesso concedido!")

# Corrigido 

# senha = ""
# while senha != "python123":
#     senha = input("Digite a senha secreta: ")
#     print("Acesso concedido!")