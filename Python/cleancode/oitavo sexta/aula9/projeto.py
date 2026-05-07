# ● O estacionamento possui um total de 500 vagas.
# ● O sistema deve manter um contador de vagas ocupadas. Se o estacionamento estiver lotado, a
# cancela de entrada não deve abrir para novos clientes (exceto para quem possui Tag de Acesso
# Rápido, pois estes têm vagas reservadas).

num_vagas = 500
import time
while num_vagas >=1:

    print("Bem-Vindo ao shopping limeira")
    tipo_acesso = int(input("Qual é o seu tipo de acesso ? \n 1- ticket: \n 2- tag: \n"))
    if tipo_acesso == 2:
            total_ticket = 15
            hora_entrada = float(input("Que horas você entrou? "))
            print("Pegue seu ticket de acesso e siga em frente!")
            num_vagas  <=1
            print("Seja Bem-Vindo. Siga em frente.")
            hora_saida = float(input("Digite a hora de saída:"))
            total_estacionamento = hora_saida - hora_entrada
            print(f"O tempo de permanência no estacionamento foi de {total_estacionamento}")
            print(f"O valor total a ser pago é de {total_ticket}")
    elif tipo_acesso == 1:
            print("pressione o botão abaixo.")
            time.sleep(3)
            print("Verificando vagas disponíveis no sistema")
            time.sleep(1)
            print("Perfeito! Vaga Disponível, siga em frente!")
    break 
tempo_estacionamento = input("Quanto tempo você ficou no estacionamento ? ")

# Saida
