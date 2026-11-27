def exibir_perfil(nome, **dados_extras):
    print(f'Nome: {nome}')
    for chave, valor in dados_extras.items():
        print(f'{chave}: {valor}')
exibir_perfil('Gabrielle', idade=25, cidade='São Paulo')
