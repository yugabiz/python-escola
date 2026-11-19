#Crie um programa que comece com uma lista vazia de
convidados. Permita que o usuário adicione 3 nomes usando o
método apropriado e, em seguida, remova um convidado que
desistiu. Exiba a lista final.#
import random
lista_de_convidados = []
for convidado in range(1, 4):
    convidado = input(f'Digite o nome do {convidado}º convidado: ')
    lista_de_convidados.append(convidado)
print(f'Lista de convidados: {lista_de_convidados}')
desistente = random.choice(lista_de_convidados)
posição = lista_de_convidados.index(desistente)
print(f'\033[31mVISH! RECEBEMOS UMA NOTÍCIA DE ÚLTIMA HORA INFORMANDO QUE ALGUÉM DESISTIU :(\033[0m')
print(f"A pessoa desistente foi: {desistente}")
print(f"A posição de {desistente} na lista era: {posição+1}")
lista_de_convidados.remove(desistente)
print(f'Nova lista de convidados: {lista_de_convidados}')
