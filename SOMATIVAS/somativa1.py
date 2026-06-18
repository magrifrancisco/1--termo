# Questão 1 

# print("Modelo da placa e do veículo")
# modeloveículo = (input("Qual o modelo do veículo"))
# placa = input("Qual é a placa do veículo")
# print("veículo", modeloveículo, placa )
# print("O veículo foi registrado, boa viagem!")

# Questão 2 

# capacidadetanque = float (input("Qual a capacidade em litros do tanque" ))
# consumo = float (input("Qual o consumo médio do caminhão" ))
# distanciatotal = capacidadetanque / consumo
# print("A distância em que o caminhão pode percorrer com o tanque cheio por litro é", distanciatotal)

# Questão 3 

# dolar = float(input("Qual o valor do frete em dólar" ))
# real = float(input("Qual o valor pago em reais" ))

# valordofrete = dolar * real
# print("O valor a ser pago pelo ferte é", valordofrete)

# Questão 4 

# rota1 = int(input("Quanto tempo leva para fazer a entrega pela rota1"))
# rota2 = int(input("Quanto tempo leva para fazer a entrega pela rota2"))
# rota3 = int(input("Quanto tempo leva para fazer a entrega pela rota3"))
# soma = rota1 + rota2 + rota3
# media = soma/ 3
# print("A média de tempo das três é", media)

# Questão 5 
# 5. Monitor de Carga: Peça o peso atual de um caminhão em toneladas.
# ○ Abaixo de 10t: "Carga Leve".
# ○ Entre 10t e 25t: "Carga padrão".
# ○ Acima de 25t: "ALERTA: Excesso de Peso!".
# carga = int(input("Quantas toneladas tem o caminhão?" ))

# if carga <10:
#     print("carga leve")
# elif carga <=25:
#     print("ALERTA: excesso de peso!")

# Questão 6
# 6. Classificador de Destino: O usuário insere o código da carga. Se começar com "N", exiba
# "Região Norte". Se começar com "S", "Região Sul". Para qualquer outro, "Região
# Internacional".

# Questão 7 
# 7. Liberação de Saída: O caminhão só pode sair se o checklist == "concluído" E o
# motorista_identificado == "sim".
# ○ Peça esses dois inputs e informe se o veículo está autorizado a iniciar a rota.

# checklist = input("O checklist foi concluído" )
# motorista = input("O motorista foi identificado" )
# if checklist == "Concluído" and motorista == "Sim":
#     print("Pode seguir em frente, boa viagem!")
# else: "não conclído, motorista não identificado"

# Questão 8 
# 8. Cálculo de Atrasos: Peça o total de entregas agendadas e o total de entregas realizadas
# com atraso.
# ○ Se o índice de atraso for maior que 10% do total, exiba "Necessário Otimizar
# Rotas", caso contrário, "Logística Eficiente".

# agendadas =  int(input("Qual é o total de entregas agendadas?" ))
# realizadasatraso = int(input("Qual é o total de entrgas feitas com atraso?" ))
# total = realizadasatraso / agendadas * 100
# print("o total é igual a", total)
# if agendadas > 10:
#     print("necessário otimizar.")
# if realizadasatraso < 10: 
#     print("Logística eficiente.")

# Questão 9 
# 9. Validação de Calibragem: Um pneu de carga deve ter pressão entre 100 PSI e 110 PSI.
# ○ Peça a medida e diga se está dentro do padrão, acima ou abaixo do recomendado.

# pressaopneucarga = float(input("Qual é a pressão do pneu de carga?" ))
# medida = float(input("Qual é a medida ?"))
# if medida < 110:
#     print("Abaixo do recomendado")
# elif medida > 110:
#     print("dentro do padrão")

# Questão 10 
# 10.Contagem de Embarque: Use um for para fazer uma contagem regressiva de 5
# até 1 para o fechamento do portão de embarque e finalize com "Portão Trancado!".

# print("fechando o portão em:")
# contagemregressiva = [5, 4, 3, 2, 1]
# for i in contagemregressiva:
#     print(f" {i}...")
# print("Portão fechado")

# Questão 11 
# 11. Somatório de Fretes (Acumulador): Use um while para pedir o valor do frete de
# vários pedidos.
# ○ O loop para quando o usuário digitar 0. No fim, mostre o faturamento total
# acumulado.

# while True:
#  valorfrete = int (input("Informe o valor do frete dos pedidos" ))
#  faturamento = int(input("Informe o valor do faturamento" ))
#  totalaculumado = valorfrete + faturamento
#  if totalacumulado == 0
#     print(f"faturamento total: {totalacumulado}")
#     break

# Questão 12 
# 12.Monitoramento de Frota: Use um for para pedir a quilometragem de 5 veículos
# diferentes.
# ○ Ao final, mostre qual foi a maior quilometragem registrada.

# Questão 13 
# 13.Sistema de Rastreio: Crie um while que peça o código de acesso do rastreador
# ("track99").
# ○ Enquanto o usuário errar, diga "Acesso Negado". Ele tem 3 tentativas. Se
# esgotar, exiba "Rastreamento Bloqueado".

# codigo = "track99"
# while codigo != "track99":
#     codigo = input("para acessar digite a senha ")
#     if codigo == "track99":
#         print("Acessando sistema", codigo)