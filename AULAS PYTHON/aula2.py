# Exemplo 1 

# for lote in range (1, 6):
#     print(f"Processando lote número {lote}...")
#     print("Qualidade verificada. [OK]")
#     print("Produção do dia finalizada!")

 # Imagine que você queira atingir uma meta de produção de 5 carros e nuemra-los

#  for carros in range (1, 6):
#     print(f"Produção de carros diárias {carros}...")

# # Exemplo 2 
# # Contar até 4 
# for i in range(5):
#    print(i)

# Exemplo 3 
# peças = ["Engrenagem", "Eixo", "Rolamento", "Parafuso", "Martelo"]
# tipospeças = ["Barra Dentada", "Porca do Eixo", "Anel Externo", "Parafuso Philips", "Materlo cabeça chata"]

# for item in peças:
#     print(f"Item em estoque: {item} + {tipospeças}")
#     for tipos in tipospeças: 
#         print(f"Minha lista de tipos de peças {tipospeças}")

# # Exemplo 4
# # Imagine a seguinte situação gostaria de ter um menu onde pudesse perguntar qual opção você deseja e a partir da seleção ele listar od produtos

# print("Loja de peças do Chicão")
# print("Bem-Vindo ao nosso Sistema")
# print("Escolha uma das o opções")
# print("1 - Peças")
# print("2 - Tipos de Peças")

# opção = int(input("Digite sua opção de pesquisa: "))

# if opção == 1: 
#     for item in peças:
#         print(f"Item em estoque: {item}")
# elif opção == 2:
#         for item2 in peças:
#             print(f"Item em estoque: {item2}")
#         print("Fim da lista")
# else:
#         print("Encerrando sitema")

# # Exercício 1 
# # Contador de Produção (for)

# for ciclo in range(1, 11):
#      print(f"Peça nº {ciclo} processando com sucesso...")
# print("Ciclo de produção concluído...")

# Exercício 2

# print("Quantidade de bananas:")
# for banana in range (1, 11):
#      print(f"Bananas {banana}")
# print("Quantidade de mangas:")     
# for mangas in range (1, 6):
#      print(f"Mangas {mangas}")
# print("Quantidade de melancias:")   
# for melancia in range (1, 11):
#      print(f"Melancias {melancia}")
# print("Quantidade de abacaxis:")     
# for abacaxi in range (1, 14):
#      print(f"Abacaxis {abacaxi}")

# # Exercício 3

# tabuada = int(input("Qual tabuada você deseja"))
# for número in range ( 1, 11):
#     resultado = tabuada * número
#     print(f"tabuada do {tabuada} X {número} = {resultado}:")
     
# Exemplo: Monitor de Temperatura (Loop Infinito Controlado)

# import time
# temperatura = 25 
# while temperatura < 40: 
#      print(f"Temperatura atual:{temperatura}°C. Sistema operando...")
#      temperatura += 3 # Simulando o aquecimento da máquina
# print("ALERTA! Temeperatura atingiu o limite. Desligando motor...")

# Exemplo: Menu de Ineração
# != diferente
# lower minúsculo
# upper maiusculo
opção = ""

while opção != "sair" and "SAIR":
     opção = input("Digite a leitura do sensor ou 'sair' para fechar: ").lower()
     if opção != "sair" and "SAIR":
          print(f"Dado '{opção}' registrado no banco de dados.")
print("Sistema encerrado.")

# and e or 
# and comparações verdadeeira e iguais
# comparações verdadeiras 

# Exercício 5
# Monitor de Pressão Crítica (while)

# pressão = 50 
# while pressão  <100:
#      pressão = int(input("digite o outro valor pressão"))
#      print(f"temperatura atual: {pressão}PSI. sistema operando")
#      print("ALERTA! pressão crítica atingida")

print("menu de séries")
print("1 - séries ação")
print("2 - séries de terror")
print("3 - séries de romance")
print("4 - séries de desenho")

série = ""

while série == "1" or "2" or "3" or "4":
    série = input("Qual tipo de série você deseja: ")

    if série == "1":
    
        print("Você escolheu série de ação")
        print("Você escolheu série de terror")
        print("Você escolheu série de romance")
        print("")