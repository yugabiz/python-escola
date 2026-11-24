# Leia o código do usuário e verifique se é igual a 1234; caso contrário, mostre “Usuário inválido!”.
# Se estiver correto, leia a senha e verifique se é igual a 9999; caso contrário, mostre “Senha incorreta”. Se ambos estiverem corretos, mostre “Acesso permitido”.

código = int(input('Digite o código de usuário: '))
if código == 1234:
    senha = int(input('Digite a senha do usuáro: '))
    if senha == 9999:
        print('Acesso Permitido')
    else:
        print('Acesso Negado')
else:
    print('Tente Novamente')
        
