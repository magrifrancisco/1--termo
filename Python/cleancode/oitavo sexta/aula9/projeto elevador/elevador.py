# Sistema de Elevador de prédio
# O prédio possui 10 andares, sendo o térreo o andar 0. O elevador pode se mover para cima ou para baixo, e tem a capacidade de transportar até 5 pessoas.
# O elevador começa no andar 0 e pode ser chamado por qualquer pessoa em qualquer andar. 
# O elevador deve se mover para o andar onde a pessoa chamou, e depois para o andar destino da pessoa.
# O elevador deve exibir uma mensagem indicando o andar atual, o número de pessoas no elevador, e as ações realizadas (subindo, descendo, parando). O programa deve continuar rodando até que o usuário decida encerrar.
 
# Levantamento de requisitos 
# Requisitos Funcionais(RF):
# O elevador pode se mover para cima e para baixo 
# O elevador pode ser chamado por qualquer pessoa em qualquer andar do prédio
# O elevador tem a capacidade de transportar até 5 pessoas
# O elevador deve ir até o andar em que a pessoa chamou e depois ir até o destino


# Requisitos Não Funcionais(RNF)
# O elevador deve exibir uma mensagem indicando o andar atual da pessoa 
# O programa deve continuar funcionando e rodando até que a pessoa que está no elevador decida parar
# O elevador começa no andar 0 

print("===================")
print("SISTEMA DE ELEVADOR")
print("===================")
import time 

terreo = 0 
andar_atual = 0
capacidade_elevador = 5 

while True:
    print(f"\nO elevador está no andar: {andar_atual}")
    interacao_botao = input("Pressione o botão para chamar o elevador ou digite sair para encerrar o sistema")
    print("O elevador tem uma capacidade total de 5 pessoas!")
    time.sleep(2)
    if interacao_botao == "Sair":
        print("Encerreando sistema!")
        break
    else: 

     pessoas = int(input("Quantas pessoas irão entrar no elevador?:"))

     if pessoas <= 5:
        print("Pode entrar, lugar disponível!")

     if pessoas > capacidade_elevador:
        print("Capacidade máxima atingida!")
        continue

     elif pessoas < capacidade_elevador:
        print("Capacidade do elevador disponível, Entre!")
        andar_atual = int(input("Qual andar você está?: "))
    andar_destino = int(input("Digite o andar de destino (0 a 10): "))

    if andar_destino > andar_atual:
        print(f"O elevador está com {pessoas} pessoas")
        print("Elevador subindo...")
        andar_atual = andar_destino
    
    elif andar_destino < andar_atual:
        print("Elevador descendo...")
        andar_atual = andar_destino


