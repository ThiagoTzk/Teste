while True:
        numero1 = input('Digite o Primeiro número: ')
        numero2 = input('Digite o Segundo número: ')
        metodo = input('Digite o Método para o calculo (M)ultiplição, (S)ubtração, (A)dição, (D)ivisão: ')

        multiplicacao = float(numero1) * float(numero2)
        subtracao = float(numero1)- float(numero2)
        adicao = float(numero1) + float(numero2)
        divisao = float(numero1) % float(numero2)

        if metodo == 'M' or metodo == 'm':
                print (f'O resultado da multiplicação de {numero1} + {numero2} é {multiplicacao:.2f}')
        elif metodo == 'S' or metodo == 's':
                print (f'O resultado da multiplicação de {numero1} + {numero2} é {subtracao:.2f}')
        elif metodo == 'A' or metodo == 'a':
                print (f'O resultado da multiplicação de {numero1} + {numero2} é {adicao:.2f}')
        elif metodo == 'D' or metodo == 'd':
                print (f'O resultado da multiplicação de {numero1} + {numero2} é {divisao:.2f}')
        else:
                print (f'Digite a letra correspondente para o calculo (M)ultiplição, (S)ubtração, (A)dição, (D)ivisão:')

        continuar = input('Deseja sair? Digite [s]im para sair ou qualquer outra coisa para continuar: ').strip().lower()
        if continuar == 's' or continuar == 'sim':
                print('Encerrando o programa. Obrigado!')
                break