# Leia as idades de 2 homens e 2 mulheres, calcule e escreva a soma da idade do homem mais velho com a mulher mais nova e o produto da idade do homem mais novo com a mulher mais velha.
# Calcule e escreva a soma das idades do homem mais velho com a mulher mais nova e o produto das idades do homem mais novo com a mulher mais velha.

h1 = int(input('Idade do primeiro homem: '))
h2 = int(input('Idade do segundo homem: '))
m1 = int(input('Idade da primeira mulher: '))
m2 = int(input('Idade da segunda mulher: '))
if h1 > h2:
    homem_velho = h1
    homem_novo = h2
else:
    homem_velho = h2
    homem_novo = h1

if m1 > m2:
    mulher_velha = m1
    mulher_nova = m2
else:
    mulher_velha = m2
    mulher_nova = m1

s = homem_velho + mulher_nova
p = homem_novo * mulher_velha
print(f'A soma é {s}.')
print(f'O produto é {p}.')
