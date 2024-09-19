import os
os.system('cls')

fila = []
operacao = input('Fila do consultório, Digite qualquer tecla para iniciar ou (s) para sair:  ')

while operacao != 's':
    if operacao == 'a':
        if len(fila) > 0:
            os.system('cls')
            atendido = fila.pop(0)
            print(f'Cliente {atendido} atendido')
        else:
            os.system('cls')
            print('Fila vazia, ninguem para atender!')
    elif operacao == 'f':
        os.system('cls')
        nome = input('Digite o nome do cliente que chegou:  ')
        os.system('cls')
        ultimo = nome
        fila.append(ultimo)
    elif operacao == 's':
        os.system('cls')
    else:
        print('Operação invalida! use apenas F, A ou S')
    print(f'fila atual {fila}')
    print('Digite F para adicionar um cliente no fim da fila')
    print('ou A apra realizar o atendimento ou S para sair')
    operacao = input('Operação(F, A ou S):  ')


print("*****************FINALIZADO*****************")