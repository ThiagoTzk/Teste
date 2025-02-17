nome = input('Digite o seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
        if tamanho_nome <= 4:
            print (f'Seu nome "{nome}" é curto')
        elif tamanho_nome >= 5 and tamanho_nome <= 6:
            print (f'Seu nome "{nome}" é normal')
        else:
            print (f'Seu nome "{nome}" é muito grande')
else: print('Digite mais de uma letra')