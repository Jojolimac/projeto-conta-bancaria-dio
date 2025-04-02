menu = '''
-   BEM VINDO AO BANCO X   -
============================
Escolha uma opção:
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

saldo = 0
limite = 500
extrato = ''
numero_de_saques = 0
LIMITE_DE_SAQUES = 3

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
        print(f'\nDepósito de R$ {valor:.2f} realizado com sucesso!\n')
    else:
        print('\nValor inválido para depósito.\n')
    return saldo, extrato

def sacar(saldo, valor, extrato, numero_de_saques):
    if valor > saldo:
        print('\nSaldo insuficiente.\n')
    elif valor > limite:
        print('\nValor acima do limite.\n')
    elif numero_de_saques >= LIMITE_DE_SAQUES:
        print('\nNúmero máximo de saques atingido.\n')
    else:
        saldo -= valor
        extrato += f'Saque: R$ {valor:.2f}\n'
        numero_de_saques += 1
        print(f'\nSaque de R$ {valor:.2f} realizado com sucesso!\n')
    return saldo, extrato, numero_de_saques

def exibir_extrato(saldo, extrato):
    print('\n================ EXTRATO ================')
    print(extrato if extrato else 'Não foram realizadas movimentações.')
    print(f'\nSaldo: R$ {saldo:.2f}')
    print('==========================================')

def main():
    global saldo, extrato, numero_de_saques
    while True:
        opcao = input(menu).strip().lower()
        if opcao == 'd':
            valor = float(input('Informe o valor do depósito: '))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == 's':
            valor = float(input('Informe o valor do saque: '))
            saldo, extrato, numero_de_saques = sacar(saldo, valor, extrato, numero_de_saques)
        elif opcao == 'e':
            exibir_extrato(saldo, extrato)
        elif opcao == 'q':
            print('\n=============== BANCO X ===============')
            print('\nObrigado por utilizar nossos serviços!')
            print('\n=======================================\n')
            break
        else:
            print('\nOpção inválida. Tente novamente.\n')

if __name__ == '__main__':
    main()