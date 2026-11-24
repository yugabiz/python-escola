# Crie uma lista de cidades, peça ao usuário o nome de uma cidade e verifique se ela está cadastrada, informando sua posição na lista ou avisando caso não seja encontrada.

cidades = ['VENEZA', 'ATENAS', 'LONDRES', 'MARACANAÚ', 'SALVADOR', 'SEUL', 'PARIS', 'NOVA YORK', 'MIAMI']
cidade = input(f'Digite a cidade que deseja encontrar: ').upper().strip()
if cidade not in cidades:
    print('Cidade não encontrada!')
else:
    print('Cidade encontrada!')
    print(f'Cidade: {cidade}')
    print(f'Posição: {cidades.index(cidade)}')
