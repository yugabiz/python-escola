código = int(input('Digite o código de usuário: '))
if código == 1234:
    senha = int(input('Digite a senha do usuáro: '))
    if senha == 9999:
        print('Acesso Permitido')
    else:
        print('Acesso Negado')
else:
    print('Tente Novamente')
        