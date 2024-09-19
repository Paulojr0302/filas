import os
os.system('cls')

ultimo = 10
fila = list(range(1, ultimo + 1))
operacao = input('Digite qualquer caractere para iniciar ou ou S para sair')

while operacao != 's':
    print(f'existem {len(fila)} clientes na fila')
    print(f'fila atual {fila}')
    print('Digite F para adicionar um cliente no fim da fila')
    print('ou A apra realizar o atendimento ou S para sair')
    if operacao == 'a':
        if len(fila) > 0:
            atendido = fila.pop(0)
            print(f'Cliente {atendido - 1} atendido')
        else:
            print('Fila vazia, ninguem para atender!')
    elif operacao == 'f':
        ultimo += 1
        fila.append(ultimo)
    elif operacao == 's':
        os.system('cls')    
        print('FIM')
    else:
        print('Operação invalida! use apenas F, A ou S')
    operacao = input('Operação(F, A ou S):  ')
