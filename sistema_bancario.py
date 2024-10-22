from datetime import datetime

saldo = 100
saques = []
depositos = []
limite_transacoes = []
horarios_transacoes = []


def atualizar_limite_transacoes():
    return len(depositos) + len(saques)


def define_horario_transacoes():
    return datetime.now()


def depositar(saldo, limite_transacoes, horarios_transacoes, valor):
    if valor <= 0:
        print("\nOperação cancelada! Não foi possível depositar a quantia informada.")
    elif atualizar_limite_transacoes() >= 10:
        print("\nSeu limite de saques e depósitos diários foi atingido!")
    else:
        saldo += valor
        depositos.append(valor)
        horarios_transacoes.append(define_horario_transacoes())
        limite_transacoes = atualizar_limite_transacoes()
        print(
            f"\nForam inseridos R${valor:.2f} na sua conta \n\nSaldo atual: R${saldo:.2f} \n \nForam realizadas {limite_transacoes} transações até agora!"
        )
    return saldo, limite_transacoes, horarios_transacoes


def sacar(saldo, limite_transacoes, horarios_transacoes, valor):
    if valor <= 0:
        print("\nOperação cancelada! Não foi possível sacar a quantia informada.")
    elif atualizar_limite_transacoes() >= 10:
        print("\nSeu limite de saques e depósitos diários foi atingido!")
    elif saldo < valor:
        print("\nOperação cancelada! Você não possui saldo!")
    else:
        if valor <= 500:
            saldo -= valor
            saques.append(valor)
            horarios_transacoes.append(define_horario_transacoes())
            limite_transacoes = atualizar_limite_transacoes()
            print(
                f"\nForam sacados R${valor:.2f} da sua conta \n\nSaldo atual: R${saldo:.2f} \n \nForam realizadas {limite_transacoes} transações até agora!"
            )
        else:
            print("\nOperação cancelada! O seu limite de saque é de R$500,00")
    return saldo, limite_transacoes, horarios_transacoes


def extrato(depositos, saques, horario_transacoes, saldo):
    if not depositos and not saques:
        print("\nSeu extrato está vazio!")
    else:
        if depositos:
            print("\nSeus depósitos:")
            for i, deposito in enumerate(depositos):
                print(
                    f"R${deposito:.2f} \nHorário do Depósito: {horarios_transacoes[i]}\n"
                )
        if saques:
            print("\nSeus saques:")
            for i, saque in enumerate(saques):
                print(
                    f"R${saque:.2f} \nHorário do Saque: {horarios_transacoes[len(depositos) + i]}\n"
                )
        if not depositos:
            print("\nAinda não foram realizados depósitos")
        if not saques:
            print("\nAinda não foram realizados saques")
    print(f"\nSaldo atual: R${saldo:.2f}")


while True:
    print(
        """\n========== MENU ==========
[1] - Realizar Deposito
[2] - Realizar Saque
[3] - Visualizar Extrato
[0] - Sair
=========================="""
    )
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        valorDeposito = float(input("\nInsira o valor a ser depositado: "))
        saldo, limite_transacoes, horarios_transacoes = depositar(
            saldo, limite_transacoes, horarios_transacoes, valorDeposito
        )
    elif opcao == 2:
        valorSaque = float(input("\nInsira o valor a ser sacado: "))
        saldo, limite_transacoes, horarios_transacoes = sacar(
            saldo, limite_transacoes, horarios_transacoes, valorSaque
        )
    elif opcao == 3:
        extrato(depositos, saques, horarios_transacoes, saldo)
    elif opcao == 0:
        print("Operação encerrada! Saindo do programa...")
        break
    else:
        print("Opção inválida")
