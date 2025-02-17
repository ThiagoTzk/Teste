entrada = input('Digite a hora números: ')
try:
    hora = int(entrada)
    
    if hora >= 0 and hora <= 11:
        print (f'Bom Dia são {hora} horas')
    elif hora >= 12 and hora <= 17:
        print (f'Boa Tarde são {hora} horas')
    elif hora >= 18 and  hora <= 23:
        print (f'Boa Noite são {hora} horas')
    else:
        print ('Não conheço essa hora.')

except:
    print('Digite apenas números inteiros')