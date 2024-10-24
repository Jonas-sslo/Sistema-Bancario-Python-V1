import re
from datetime import datetime

saldo = 100
saques = []
depositos = []
limite_transacoes = []
horarios_transacoes = []
usuarios = []
numero_conta = 1


def validar_data(nascimento):
    # Formatação da Data
    try:
        data_nascimento = datetime.strptime(nascimento, "%d/%m/%Y")
        return data_nascimento
    except ValueError:
        print("\nA data de nascimento informada não está seguindo os padrões.")
        return None


def validar_endereco(endereco):
    # Formatação do Endereço
    partes = [parte.strip() for parte in endereco.split("-")]

    if len(partes) != 5:
        print("\nO formato inserido não corresponde ao informado.")
        return None
    elif (
    # Verificação para permitir apenas letras
        not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$", partes[0])
        and (not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$", partes[2]))
        and (not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$", partes[3]))
    ):
        print("\nApenas são permitidos letras nesse campo.")
        return None
    # Verificação para permitir apenas números
    elif not partes[1].isdigit() or (int(partes[1]) <= 0):
        print("\nApenas são permitidos números nesse campo.")
        return None
    # Verificação do formato da UF
    elif not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$", partes[4]) and (partes[4] != 2):
        print("\nO formato inserido não corresponde ao informado.")
        return None

    endereco = {
        "logradouro": partes[0],
        "numero": partes[1],
        "bairro": partes[2],
        "cidade": partes[3],
        "uf": partes[4],
    }

    return endereco


def cadastrar_usuario(nome, nascimento, cpf, endereco):
    cpf = re.sub(r"\D", "", cpf) # Permite apenas números
    data_nascimento = validar_data(nascimento)
    endereco_verificado = validar_endereco(endereco)

    # Validação do nome
    if not re.match(r"^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$", nome) or (len(nome) > 30):
        print("\nEsse não é um nome válido.")
        return
    # Validação do CPF
    elif len(cpf) != 11:
        print("\nCPF inválido!")
        return
    # Validação da data de nascimento
    elif data_nascimento is None:
        return
    # Validação do endereço
    elif endereco_verificado is None:
        return

    # Validação de CPF duplicado
    for usuario in usuarios:
        if cpf in usuario:
            print("\nUm usuário com esse CPF já está cadastrado.")
            return

    usuarios.append(
        {
            cpf: {
                "nome": nome,
                "nascimento": data_nascimento.strftime("%d/%m/%Y"),
                "endereco": endereco_verificado,
                "contas": [],
            }
        }
    )
    print(f"\nO usuário {nome} foi cadastrado com sucesso.")
    return usuarios


def criar_conta_corrente(cpf_usuario, numero_conta):
    for usuario in usuarios:
        if cpf_usuario in usuario:
            # Criação do dicionário da conta
            conta = {
                "Agência": "0001",
                "Número da Conta": numero_conta,
            }
            usuario[cpf_usuario]["contas"].append(conta)
            print(f"\nConta criada com sucesso! Número da conta: {numero_conta}")
            return numero_conta + 1
    print("\nUsuário não encontrado!")
    return numero_conta


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


def extrato(depositos, saques, saldo):
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
[1] - Cadastrar Usuário
[2] - Criar Conta Corrente
[3] - Realizar Deposito
[4] - Realizar Saque
[5] - Visualizar Extrato
[0] - Sair
=========================="""
    )
    opcao = int(input("Escolha uma opção: "))
    # Cadastro do Usuário
    if opcao == 1:
        nome_usuario = input("\nInsira o nome do usuário: ")
        nascimento_usuario = input("Insira a sua data de nascimento (%d/%m/%Y): ")
        cpf_usuario = input("Insira o seu CPF (apenas os digítos): ")
        endereco_usuario = input(
            "Insira o seu endereco (logradouro-número-bairro-cidade-UF:): "
        )
        cadastrar_usuario(
            nome_usuario, nascimento_usuario, cpf_usuario, endereco_usuario
        )
    # Criação da Conta Corrente
    elif opcao == 2:
        cpf_usuario = input("\nInsira o CPF do usuário dono da conta: ")
        numero_conta = criar_conta_corrente(cpf_usuario, numero_conta)
    # Saque
    elif opcao == 3:
        conta_usuario = input(
            "\nInsira o número da sua conta: "
        )  # associar com o usuario
        valorDeposito = float(input("\nInsira o valor a ser depositado: "))
        saldo, limite_transacoes, horarios_transacoes = depositar(
            saldo, limite_transacoes, horarios_transacoes, valorDeposito
        )
    # Depósito
    elif opcao == 4:
        valorSaque = float(input("\nInsira o valor a ser sacado: "))
        saldo, limite_transacoes, horarios_transacoes = sacar(
            saldo, limite_transacoes, horarios_transacoes, valorSaque
        )
    # Mostrar o extrato (pegar extrato de todas as contas do usuário)
    elif opcao == 5:
        extrato(depositos, saques, saldo)
    # Sair
    elif opcao == 0:
        print("Operação encerrada! Saindo do programa...")
        break
    else:
        print("Opção inválida")
