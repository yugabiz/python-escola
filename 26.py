números = []
pares = []
for número in range(1, 11):
    número = int(input(f'Digite o {número}º número: '))
    números.append(número)
print('     LISTA DE NÚMEROS    ')
print(f'{números}')
for número in números:
    if número % 2 == 0:
        pares.append(número)
print(f'    LISTA SOMENTE COM NÚMEROS PARES     ')
print(f'{pares}')
