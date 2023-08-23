#!/bin/python3
import os
from datetime import datetime
menu = 0
saldo = float(1000)
extrato_log = []
q_saques = 1
limite_diario = 500
LIMITE_SAQUES = 3
usuarios = []
contas = []

#criar usuário (nome, data de nascimento, cpf e endereço(lagradouro, numero, bairro e cidade/estado))
#criar conta corrente - que será vinculada ao cliente (agencia, n da conta e usuário) (o usuario pode ter várias contas - sem restrição)
#listar contas - extra
# excluir conta - extra

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = verificar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

def verificar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def deposito():
    global saldo, extrato_log
    dep = float(0)
    while True:
        print(f'''
        {' Deposito '.center(50,'=')}
        ={' Digite o valor em reais'.center(48,' ')}=
        ={' que deseja depositar'.center(48,' ')}=
        {'='.center(50,'=')}
        ''')
        dep = float(input(f'R$ '))
        os.system('cls')
        if dep >= 0:
            saldo += dep
            extrato_log.append(f'- Deposito de R$ {dep:.2f} reais.')
            print('*'.center(50,'*'))
            print(' Deposito realizado com sucesso! '.center(50,'*'))
            print('*'.center(50,'*'))
            input('\nPressione ENTER para voltar ao menu principal.')
            os.system('cls')
            break
        elif dep < 0:
            print('*'.center(50,'*'))
            print(' Você está tentando depositar um valor negativo '.center(50,'*'))
            print(' Por favor, tente novamente. '.center(50,'*'))
            print('*'.center(50,'*'))
            input('Pressione ENTER para voltar ao menu inicial.')
            os.system('cls')
            break

def saque():
    global saldo, extrato_log, limite_diario, q_saques, LIMITE_SAQUES
    valor_do_saque = float(0)
    while True:
        print(f'''
        {' Saque '.center(50,'=')}
        ={' Digite o valor em reais'.center(48,' ')}=
        ={' que deseja sacar'.center(48,' ')}=
        {'='.center(50,'=')}
        ''')
        valor_do_saque = float(input('R$ '))
        os.system('cls')
        if q_saques > LIMITE_SAQUES:
            print('*'.center(50,'*'))
            print('Infelizmente você atingiu o limite de saques(3).'.center(50,'*'))
            print(' Pedimos que aguarde até o dia seguinte, ou, em '.center(50,'*'))
            print(' caso de emergência, contate seu gerente. '.center(50,'*'))
            print('*'.center(50,'*'))
            input('Pressione ENTER para voltar ao menu inicial.')
            os.system('cls')
            break
        else:
            if valor_do_saque < 0:
                print('*'.center(50,'*'))
                print(' Você está tentando sacar um valor negativo. Por favor, tente novamente. '.center(50,'*'))
                print('*'.center(50,'*'))
                input('Pressione ENTER para voltar ao menu inicial.')
                os.system('cls')
                break
            elif valor_do_saque > 500:
                print('*'.center(50,'*'))
                print(' Somente é permitido o saque de 500 reais '.center(50,'*'))
                print(' por transação, tente novamente. '.center(50,'*'))
                print('*'.center(50,'*'))
                input('Pressione ENTER para voltar ao menu inicial.')
                os.system('cls')
                break
            elif valor_do_saque > saldo:
                print('*'.center(50,'*'))
                print(' Saldo insuficiente, caso seja algum erro pedimos que retire '.center(50,'*'))
                print(' um extrato bancário e procure seu gerente. '.center(50,'*'))
                print('*'.center(50,'*'))
                input('Pressione ENTER para voltar ao menu inicial.')
                os.system('cls')
                break
            else:
                saldo -= valor_do_saque
                extrato_log.append(f'- Saque de R$ {valor_do_saque:.2f} reais.')
                print('*'.center(50,'*'))
                print(' Saque realizado com sucesso! '.center(50,'*'))
                print('*'.center(50,'*'))
                q_saques += 1
                input('Pressione ENTER para voltar ao menu inicial.')
                os.system('cls')
                break

def extrato():
    imprimir = '\n'.join(extrato_log)
    data = datetime.now() 
    data_formatada = data.strftime('%d-%m-%Y - %H:%M')
    if extrato_log == []:
        print('Não há movimentações na conta.')
        input('Pressione ENTER para voltar ao menu inicial.')
    else:
        print(f' Extrato '.center(40,'='))
        print(f'Data: {data_formatada}\n')
        print(imprimir)
        print(f'-'.center(35,'-'))
        print(f'Saldo atual: R$ {saldo:.2f}')
        print(f' '.center(40,'='))
        input('Pressione ENTER para voltar ao menu inicial.')
    os.system('cls')

while True:
    print(f'''
        {' Menu '.center(50,'=')}
        ={' Selecione a operação que deseja'.center(48,' ')}=
        ={' realizar conforme o número:'.center(48,' ')}=
        ={' '.center(48,' ')}=
        ={'[1] Deposito'.center(48,' ')}=
        ={' '.center(48,' ')}=
        ={'[2] Saque'.center(48,' ')}=
        ={' '.center(48,' ')}=
        ={'[3] Extrato'.center(48,' ')}=
        ={' '.center(48,' ')}=
        ={'[4] Criar Usuário'.center(48,' ')}=
        ={' '.center(48,' ')}=
        ={'[0] Encerrar'.center(48,' ')}=
        ={' '.center(48,' ')}=
        {'='.center(50,'=')}
    ''')
    menu = int(input('Opção: '))
    os.system('cls')
    if menu > 4:
        print('Opção incorreta,tente novamente.')
    elif menu < 0:
        print('Erro, reinicie o programa.')
        break
    else:
        if menu == 1:
            deposito()
        elif menu == 2:
            saque()
        elif menu == 3:
            extrato()
        elif menu == 4:
            criar_usuario(usuarios)
        elif menu == 0:
            os.system('cls')
            print('Encerrando...')
            break