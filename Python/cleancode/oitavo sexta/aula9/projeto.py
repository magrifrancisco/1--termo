# ● O estacionamento possui um total de 500 vagas.
# ● O sistema deve manter um contador de vagas ocupadas. Se o estacionamento estiver lotado, a
# cancela de entrada não deve abrir para novos clientes (exceto para quem possui Tag de Acesso
# Rápido, pois estes têm vagas reservadas).


total_ticket = 15
hora_extra = 3
num_vagas = 500
import time
while True:


    print("Bem-Vindo ao shopping limeira")
    hora_entrada = float(input("Que horas você entrou? "))
    tipo_acesso = int(input("Qual é o seu tipo de acesso ? \n 1- ticket: \n 2- tag: \n 3- cliente especial: \n 4- Sair: \n"))
    if tipo_acesso == 2:

        print("Pegue seu ticket de acesso e siga em frente!")
        num_vagas  <=1
        print("Seja Bem-Vindo. Siga em frente.")
        hora_saida = float(input("Digite a hora de saída:"))
        total_estacionamento = hora_saida - hora_entrada
        print(f"O tempo de permanência no estacionamento foi de {total_estacionamento}")
        print(f"O valor total a ser pago é de {total_ticket}")
        print("Saída Liberada, Volte Sempre!")
        continue
    elif tipo_acesso == 1:
        print("pressione o botão abaixo.")
        time.sleep(3)
        print("Verificando vagas disponíveis no sistema")
        time.sleep(1)
        print("Perfeito! Vaga Disponível, siga em frente!")
    if tipo_acesso == 3:
        valor_tag = total_ticket + (total_ticket * 0.1)
        print("Você terá 10% de desconto! ")
        print(f"O valor a ser pago será{valor_tag}")
        tempo_estacionamento = float(input("Quanto tempo você ficou no estacionamento ? "))
    if tempo_estacionamento <= 0.15:
        print("Você não terá que pagar pelo estacionamento! ")
    elif tempo_estacionamento == 3:
        print("você terá que pagar 15,00 pelo estacionamento! ")
    elif tempo_estacionamento > 3:
        total_ticket = 15
        print(f"Será cobrado um valor adicional por hora {(tempo_estacionamento * total_ticket) + 3}")
        break

    else:
        print("Saída liberada!")
        break    


                
