saldo = 100
contagem_saques = 0
LIMITE_SAQUES = 3
saques = []
depositos = []


def depositar(saldo, valor):
    if valor <= 0:
        print("\nOperação cancelada! Não foi possível depositar a quantia informada.")
    else:
        saldo += valor
        depositos.append(valor)
        print(
            f"\nForam inseridos R${valor:.2f} na sua conta \nSaldo atual: R${saldo:.2f}"
        )
    return saldo


def sacar(saldo, contagem_saques, valor):
    if valor <= 0:
        print("\nOperação cancelada! Não foi possível sacar a quantia informada.")
    elif contagem_saques >= LIMITE_SAQUES:
        print("\nSeu limite de saques diários foi atingido!")
    elif saldo < valor:
        print("\nOperação cancelada! Você não possui saldo!")
    else:
        if valor <= 500:
            saldo -= valor
            contagem_saques += 1
            saques.append(valor)
            print(
               f"\nForam sacados R${valor:.2f} da sua conta \nSaldo atual: R${saldo:.2f} \n \nForam realizados {contagem_saques} até agora!"
            )
        else:
            print("\nOperação cancelada! O seu limite de saque é de R$500,00")
    return saldo, contagem_saques


def extrato(depositos, saques, saldo):
    if (not depositos) and (not saques):
        print("\nSeu extrato está vazio!")
    else:
        if depositos:
            print("\nSeus depósitos:")
            for deposito in depositos:
                print(f"R${deposito:.2f}")
        if saques:
            print("\nSeus saques:")
            for saque in saques:
                print(f"R${saque:.2f}")

        if not depositos:
            print("\nAinda não foram realizados depósitos")
        if not saques:
            print("\nAinda não foram realizados saques")

    print(f"\nSaldo atual: R${saldo:.2f}")


while True:

    print(
        f""" 
========== MENU ==========
[1] - Realizar Deposito
[2] - Realizar Saque
[3] - Visualizar Extrato
[0] - Sair
==========================
    """
    )

    opcao = int(input(f"Escolha uma opção: "))

    if opcao == 1:
        valorDeposito = float(input("\nInsira o valor a ser depositado: "))
        saldo = depositar(saldo, valorDeposito)
    elif opcao == 2:
        valorSaque = float(input("\nInsira o valor a ser sacado: "))
        saldo, contagem_saques= sacar(saldo, contagem_saques, valorSaque)
    elif opcao == 3:
        extrato(depositos, saques, saldo)
    elif opcao == 0:
        print("Operação encerrada! Saindo do programa...")
        break
    else:
        print("Opção inválida")