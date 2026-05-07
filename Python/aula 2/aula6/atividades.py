# lista de temperaturas lidas pelo sensor por minuto
# leituras = [70, 75, 82, 98, 110, 85, 80]
# baixos = [50, 55, 52, 30, 20, 15, 10]

# for temp in leituras:
#     if temp > 100:
#         print(f"CRÍTICO: {temp}°C detectado! Acionando parada de emergência.")
#         break # O loop para aqui e NÃO lê os próximos valores (85 e 80)
#     for temp1 in baixos:
#         if temp1 < 50:
#          print(f"CRÍTICO: {temp}°C detectado! Acionando parada de emergência.")
#     break
# else:
#     print(f"Temperatura está em {temp1}°C. Operação com valores baixo.")
#     print("Checar Sistema. Aguardando manuenção.")
#     # Cenário 2
#     # Adicionar uma outra condição para temperatura abaixo de 50 e quando chegar até 10 parar 

# for temp in leituras:
#    if temp > 100:
#       print(f"CRÍTICO:{temp}°C. Detectado! Acionando parada de emergência.")
#       break # O loop para aqui 


# materiais = ["metal", "metal", "plastico", "metal", "vidro", "metal"]
# for peca in materiais:
#    if peca != "metal":
#       print(f"Aviso: Peça de {peca} detectada. Desviando para descarte...")
#       continue # Pula o restante do código abaixo e vai para a próxima peça

#    # Este código só roda se a peça for de metal
#    print(f"Processando peça de {peca}. Furando e polindo...")

#    print("Fim do lote de produção.")

# # Exercício 1
# # Temte criar um código que conte de 1 a 10, mas use o continue para não imprimir o número 5 (Simulando uma falha de sensor específica no item 5)

# for numero in range (1, 11):
#     if numero == 5:
#         print(f"AVISO: falha detectada no sensor de {numero}. ")
#         continue
#     print(f"sensor de {numero} contando")
# print("fim da contagem")

# # Exercício 2 
# # Simule um semaforo com parada para cada cor. Determine um tempo que deseja para que quando mudar para tal cor ele represente uma pausa

# from time import sleep
# for i in range (1, 11):

#     sleep(0.5)
#     print("Verde")
# print("Siga em frente")

# for i in range (8):

#     sleep(0.5)
#     print("Vermelho")
# print("Atençao")

# for i in range (6):

#     sleep(1)
#     print("Amarelo")
# print("Espere.")

# # Exercício 3 - Soma de Cargas de Energia (for)

# maquinas = ['maquina', 'maquina', 'maquina', 'maquina', 'maquina']

# for maquina in maquinas:
#     consumo = (input(f"Qual a quantidade de kwh de cada máquina{maquina}"))
#     print(maquina)
#     totalkwh = consumo + maquina
#     print(f"{totalkwh}") 

#     # Exercício 4 - Identificador de Peças Defeituosas (for + if)

#     medidas = [50.1, 49.8, 52.0, 48.5]
#     for pecas in medidas: 
#         if pecas > 50: 
#             print(f"Peça {pecas} Aprovada..:)")
#         else:
#             print(f"Peça {pecas} Rejeitada")

# # Exercício 5 

# Sacos = [49.5, 50.0, 51,2, 48.9, 50.5, 47.8]
# for peso in Sacos:
#     if 49.0 <= peso <= 51.0:
#         print(f"Saco com peso {peso}kg: Aceitável")
#     else:
#         print(f"Saco com peso {peso}kg: Rejeitado - Fora do limite aceitável")

# # Exercício 6: Sistema Inteligente de Manutenção

# estufa = 0

# while estufa < 5: 
#     temp = float(input("Digite a temperatura da estufa:"))
#     if temp < 0: 
#         print("Erro de leitura no sensor. Por favor, insira uma temperatura válida.")
#         continue
#     elif temp > 150: 
#         print("ALERTA CRÍTICO: Risco de Explosão!")
#         break
#     else:
#         print(f"Peça [estufa + 1] processada com sucesso a {temp}°C.")
#         estufa += 1

# # Exercício 7 - Monitoramento de Vibração

