# Crie uma lista com 5 itens de supermercado informados pelo usuário e exiba o primeiro e o último item da lista.

lista_de_compras = []
for itens in range(1, 6):
    itens = input(f'Digite o {itens}º item da lista: ')
    lista_de_compras.append(itens)
print(f'Todos os itens informados foi {lista_de_compras}')
print(f'O primeiro item da lista: {lista_de_compras[0]}')
print(f'O último item da lista: {lista_de_compras[-1]}')
