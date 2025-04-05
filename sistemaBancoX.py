# Banco X - Sistema de Gerenciamento de Conta
import textwrap
# Sistema de gerenciamento de contas bancárias com funcionalidades de cadastro de usuários, contas, depósitos, saques e extratos.

def menu():
    menu = '''\n
    -   BEM VINDO AO BANCO X   -
    ============================
    Escolha uma opção:
    
    [d] \tDepositar
    [s] \tSacar
    [e] \tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [q] \tSair
    
    ============================
    Digite a opção desejada:

    => '''
    return input(textwrap.dedent(menu))

def cadastrar_conta(usuarios, contas, cpf):
    if cpf in usuarios:
        if cpf not in contas:
            agencia = '0001'
            numero_conta = len(contas) + 1
            contas[cpf] = {numero_conta}
            print(f'\nConta cadastrada com sucesso! Agencia:{agencia} Número da conta: {numero_conta}\n')
        else:
            print('\nConta já cadastrada.\n')
    else:
        print('\nUsuário não cadastrado. Cadastre o usuário primeiro.\n')

def criar_usuario(usuarios):
    cpf = input('Informe o CPF (somente números): ')
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print('\nUsuário já cadastrado.\n')
        return
    
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    endereco = input('Informe o endereço (logradouro, número - bairro - cidade/estado): ')
    
    usuarios.append({'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco})
    
    print(f'\nUsuário {nome} cadastrado com sucesso!\n')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuário: ')
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print (f'\nConta criada com sucesso! Agência: {agencia} Número da conta: {numero_conta}\n')
        
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}
    
    print('\nUsuário não encontrado.\n')

def listar_contas(contas):
    if not contas:
        print('\nNenhuma conta cadastrada.\n')
        return

    print('=' * 100)
    for conta in contas:
        linha = f'''\
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        '''
        print(textwrap.dedent(linha))
        print('-' * 100)
    print('=' * 100)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito:\tR$ {valor:.2f}\n'
        print(f'\nDepósito de R$ {valor:.2f} realizado com sucesso!\n')
    else:
        print('\nValor inválido para depósito.\n')
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, limite_saques, numero_de_saques):
    if valor > saldo:
        print('\nSaldo insuficiente.\n')
    elif valor > limite:
        print('\nValor acima do limite.\n')
    elif numero_de_saques >= limite_saques:
        print('\nNúmero máximo de saques atingido.\n')
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque:\t\tR$ {valor:.2f}\n'
        numero_de_saques += 1
        print(f'\nSaque de R$ {valor:.2f} realizado com sucesso!\n')
    else:
        print('\nValor inválido para saque.\n')
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print('\n================ EXTRATO ================')
    print(extrato if extrato else 'Não foram realizadas movimentações.')
    print(f'\nSaldo:\t\tR$ {saldo:.2f}')
    print('==========================================')

def main():
    LIMITE_DE_SAQUES = 3
    AGENCIA = '0001'
    
    saldo = 0
    limite = 500
    extrato = ''
    numero_de_saques = 0
    usuarios = []
    contas = []
    

    while True:
        opcao = menu()
        
        if opcao == 'd':
            valor = float(input('Informe o valor do depósito: '))
            
            saldo, extrato = depositar(saldo, valor, extrato)
            
        elif opcao == 's':
            valor = float(input('Informe o valor do saque: '))
            
            saldo, extrato, = sacar(saldo=saldo, 
                                    valor=valor, 
                                    extrato=extrato, numero_de_saques=numero_de_saques,
                                    limite=limite, limite_saques=LIMITE_DE_SAQUES,
                                    )
        elif opcao == 'e':
            exibir_extrato(saldo, extrato=extrato)
            
        elif opcao == 'nu':
            criar_usuario(usuarios)
            
        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)
                
        elif opcao == 'lc':
            listar_contas(contas)
                
        elif opcao == 'q':
            print('\n=============== BANCO X ===============')
            print('\nObrigado por utilizar nossos serviços!')
            print('\n=======================================\n')
            break
        else:
            print('\nOpção inválida. Tente novamente.\n')

if __name__ == '__main__':
    main()