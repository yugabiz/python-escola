cidades = ['VENEZA', 'ATENAS', 'LONDRES', 'MARACANAÚ', 'SALVADOR', 'SEUL', 'PARIS', 'NOVA YORK', 'MIAMI']
cidade = input(f'Digite a cidade que deseja encontrar: ').upper().strip()
if cidade not in cidades:
    print('Cidade não encontrada!')
else:
    print('Cidade encontrada!')
    print(f'Cidade: {cidade}')
    print(f'Posição: {cidades.index(cidade)}')
