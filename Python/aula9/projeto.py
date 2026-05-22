
# SISTEMA DE ESTACIONAMENTO - SHOPPING

import time

num_vagas = 500
vagas_tag = 50

valor_fixo = 15
hora_extra = 3


while True:

    print(" BEM-VINDO AO SHOPPING LIMEIRA ")

    print("1 - Ticket")
    print("2 - TAG")
    print("3 - Cliente Especial")
    print("4 - Sair")

    tipo_acesso = int(
        input("Qual é o seu tipo de acesso? ")
    )

    if tipo_acesso == 4:

        print("Sistema encerrado.")
        break


    elif tipo_acesso == 1:

        print("\nPressione o botão abaixo.")
        time.sleep(2)

        if num_vagas <= vagas_tag:

            print("Estacionamento lotado.")
            continue

        print("Vaga disponível.")
        num_vagas -= 1


    elif tipo_acesso == 2:

        print("\nVerificando TAG...")
        time.sleep(2)

        if num_vagas <= 0 and vagas_tag <= 0:

            print("Estacionamento lotado.")
            continue

        print("TAG validada com sucesso.")
        vagas_tag -= 1


    elif tipo_acesso == 3:

        print("\nCliente especial identificado.")


    else:

        print("Opção inválida.")
        continue


    hora_entrada = float(
        input("Digite a hora de entrada: ")
    )

    hora_saida = float(
        input("Digite a hora de saída: ")
    )

    tempo_estacionamento = (
        hora_saida - hora_entrada
    )

    print(
        f"Tempo no estacionamento: "
        f"{tempo_estacionamento} horas"
    )


    if tempo_estacionamento <= 0.15:

        total_ticket = 0

    elif tempo_estacionamento <= 3:

        total_ticket = valor_fixo

    else:

        total_ticket = (
            valor_fixo +
            ((tempo_estacionamento - 3)
            * hora_extra)
        )


    if tipo_acesso == 2:

        total_ticket = (
            total_ticket -
            (total_ticket * 0.10)
        )

        print(
            "Cliente TAG possui "
            "10% de desconto."
        )


    print(
        f"Valor total: "
        f"R$ {total_ticket:.2f}"
    )


    pagamento = input(
        "Pagamento realizado? (s/n): "
    )

    if pagamento == "s":

        print("Pagamento confirmado.")
        print("Saída liberada.")

        if tipo_acesso == 1:

            num_vagas += 1

        elif tipo_acesso == 2:

            vagas_tag += 1

    else:

        print("Pagamento pendente.")
        print("Cancela fechada.")
