import os
from datetime import datetime

def menu(): 
    print("""
======= SISTEMA BANCÁRIO INTERMEDIÁRIO =======
| [1] - Depositar                       |
| [2] - Sacar                           |
| [3] - Extrato                         |
| [4] - Cadastrar Cliente               |
| [5] - Visualizar Cliente              |
| [6] - Criar Conta Corrente            |
| [7] - Visualizar Conta Corrente       |
| [8] - Sair                            |
=======================================
""")

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

NUMERO_AGENCIA = "0001"
conta_corrente = 0


listaCadastroCliente = []
listaContaBancaria = []

#Função para cadastro de cliente 
def cadastroCliente():
    global listaCadastroCliente
    print("\n======= CADASTRO CLIENTE ==========\n")
    cpfCliente = input("Digite o CPF do cliente: ")

    # Verifica se o CPF já está cadastrado
    for cliente in listaCadastroCliente:
        if cliente[0] == cpfCliente:
            print("\nCliente com este CPF já tem cadastro")
            return

    # Se não está cadastrado, coleta os dados
    nomeCliente = input("\nDigite o nome do cliente: ")
    dataAniversarioCliente = input("\nDigite data de aniversário (dd/mm/aaaa): ")
    
    try:
        dataAniversarioFormatada = datetime.strptime(dataAniversarioCliente, "%d/%m/%Y")
    except ValueError:
        print("\nData de aniversário inválida. Use o formato dd/mm/aaaa.")
        return
    
    print("\n======= ENDEREÇO CLIENTE ==========\n")
    enderecoCliente = input("Digite o endereço [Logradouro - Bairro - Cidade/Estado]: ")

    # Agrupa os dados em uma lista e adiciona à lista principal
    clienteCadastro = [cpfCliente, nomeCliente, dataAniversarioFormatada, enderecoCliente]
    listaCadastroCliente.append(clienteCadastro)
    print("\nCliente cadastrado com sucesso!\n")

#Função para visualizar Cliente
def visiualizarCliente():
    global listaCadastroCliente
    cpfCliente = input("Digite o CPF do cliente a ser buscado: ")

    # Busca pelo cliente na lista
    for cliente in listaCadastroCliente:
        if cliente[0] == cpfCliente:
            print("\n===== CLIENTE ENCONTRADO =====")
            print(f"CPF: {cliente[0]}")
            print(f"Nome: {cliente[1]}")
            print(f"Data de aniversário: {cliente[2].strftime('%d/%m/%Y')}")
            print(f"Endereço: {cliente[3]}")
            print("=================================")
            return

    # Caso o cliente não seja encontrado
    print("\nCliente não encontrado!.\n")


#Função para cadastro de Conta bancária
def CadastroContaBancaria():
    global listaCadastroCliente
    global listaContaBancaria
    global NUMERO_AGENCIA
    global conta_corrente
    
    print("\n=================== CADASTRO DE CONTA CORRENTE =================\n")
    CPFCliente = input("Digite o CPF do cliente para criação de Conta: ")

    nome_Cliente = None

    # Procura o CPF do cliente na lista de cadastro
    for cliente in listaCadastroCliente:
        if cliente[0] == CPFCliente:  # Assumindo que o CPF está no índice 1
            nome_Cliente = cliente[1]  # O nome está no índice 0
            break

    if nome_Cliente is None:
        print("==============================================================")
        print("\nCliente não encontrado/ Cliente não cadastrado no sistema. Verifique o CPF informado.\n")
        print("==================================================================")
        return
    
    # Cria a conta bancária para o cliente
    ListaConta = [conta_corrente + 1, NUMERO_AGENCIA, CPFCliente, nome_Cliente]
    
    # Adiciona a nova conta à lista de contas bancárias
    listaContaBancaria.append(ListaConta)
    print("\n")
    print("===========================")
    print("CONTA CRIADA COM SUCESSO!")
    print("===========================")
    print(f"Número da Conta: {conta_corrente + 1}")
    print(f"Agência: {NUMERO_AGENCIA}")
    print(f"CPF: {CPFCliente}")
    print(f"Nome: {nome_Cliente}\n")

    # Atualiza o número da conta corrente
    conta_corrente += 1

def visualizarContaBancaria():
    global listaContaBancaria
    cpfCliente = input("Digite o CPF do cliente a ser buscado: ")

    # Itera sobre a lista de contas bancárias
    for conta in listaContaBancaria:
        # Verifica se o CPF na conta corresponde ao CPF buscado
        if conta[2] == cpfCliente:  # Índice 2 representando o CPF
            print("\n===== CONTA ENCONTRADA =====")
            print("\n")
            print("-----------CONTAS------------\n")
            print(f"CONTA: {conta[0]}") 
            print(f"AGÊNCIA: {conta[1]}")  
            print(f"CPF: {conta[2]}")  
            print(f"Nome: {conta[3]}")  
            print("=================================")
                
#Função para depósito de Saldo
def depositar(valorDepositado): 
    global saldo #declaração para variavel global ser contemplada na função
    global extrato
    if valorDepositado > 0:
        saldo+=valorDepositado 
        print(f"\nO valor de {valorDepositado} R$ foi adicionado com sucesso na conta")
        extrato += f"Depósito: R$ {valorDepositado:.2f}\n"
    else:
        print("\nApenas valores positivos devem ser insderidos no Depósito")

#Função para sacar Saldo
def sacar(valorSacar):
    global numero_saques
    global saldo
    global numero_saques
    global limite
    global extrato
    global LIMITE_SAQUES
    if numero_saques < LIMITE_SAQUES:
        if saldo >= valorSacar and valorSacar<=limite:
            saldo-= valorSacar
            numero_saques += 1
            print(f"\nO valor de {valorSacar} R$ foi sacado com sucesso na sua conta")
            extrato += f"Saque: R$ {valorSacar:.2f}\n"
        elif saldo< valorSacar:
            print("\nSaldo da conta é insuficiente")
        else:
            print("\nValor a ser sacado é superior ao limite máximo de 500 R$")
    else:
        print("\nVocê excedeu o limite diário de saques")


def extratos( saldo, / , *, extrato):
    print("\n-------EXTRATO------")
    print("\nO seu extrato")
    if not extrato:
        print("\nNão há movimentação na conta!")
    else:
        print(f"\n{extrato}")
        print(f"\nO saldo total da sua conta é: {saldo} R$")


while True:
    menu()
    opcao = int(input("Digite a opção: "))

    os.system("cls")

    if opcao == 1:
        os.system("cls")
        print("\n-------DEPÓSITO-------")
        valorDeposito=float(input("\nInforme o valor a ser depositado na conta: "))
        depositar(valorDeposito)
    elif opcao == 2:
        os.system("cls")
        print("\n-------SAQUE--------")
        valorSacar=float(input("\nInforme o valor a ser sacado da conta: "))
        sacar(valorSacar)
    elif opcao == 3:
        extratos(saldo, extrato=extrato)
    elif opcao == 4:
        os.system("cls")
        cadastroCliente()

    elif opcao == 5:
        os.system("cls")
        visiualizarCliente()
    elif opcao == 6:
        os.system("cls")
        CadastroContaBancaria()
    
    elif opcao == 7:
        os.system("cls")
        visualizarContaBancaria()

    elif opcao == 8:
        break

    else:
        print("\nOpção digitada é inválida!, Por favor digite a operação adequada")