# Crie um programa que leia a quantidade (em Kg) de morangos e maças compradas e exiba o valor total a pagar.

morango = float(input('Digite em (kg)s a quantidade de morango(s): '))
maça = float(input('Digite em kg(s) a quantidade de maça(s): '))
if morango > 5:
    pmo = morango * 2.20
else:
    pmo = morango * 2.50
if maça > 5:
    pma = maça * 1.50
else:
    pma = maça * 1.80
total_de_frutas = morango + maça
valor = pma + pmo
if total_de_frutas > 8 or valor > 25:
    total = valor - (0.10 * valor)
else:
    total = valor
print(f'A quantidade em kg(s) de frutas compradas é de {total_de_frutas:.1f}kg e o valor total a ser pago será de {total:.2f}')
