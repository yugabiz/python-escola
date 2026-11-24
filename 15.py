# Ler um valor inteiro (Aceitando somente valores entre 1 e 10) e escrever a tabuada de 1 a 10 do valor lido.

n = int(input('Digite um número de (1 a 10) para ver a tabuada: '))
c = 1
while n < 1 or n > 10:
    n = int(input('Número Inválido. Tente Novamente. \nDigite um número de (1 a 10): '))
    print(f'TABUADA DO NÚMERO {n}')
while c <= 10:
    print(f'{n} x {c} = {n*c}')
    c += 1
