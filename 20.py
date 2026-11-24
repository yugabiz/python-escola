# Leia as temperaturas médias dos 12 meses, armazene-as em uma lista, calcule a média anual e mostre as temperaturas acima da média, indicando seus respectivos meses.

temperaturas = []
soma_temp = 0
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
print('\033[33m----- INDICADOR MENSAL DE TEMPERATURAS -----\033[m')
for mês in range(12):
    temperatura = float(input(f'{meses[mês]}: '))
    soma_temp += temperatura
    temperaturas.append(temperatura)
média = soma_temp / 12
print(f'A média anual dessas temperaturas foi {média:.1f}°')
print('\033[31mMESES EM QUE A TEMPERATURA ULTRAPASSOU A MÉDIA ANUAL\033[m')
for mês in range(12):
    if temperaturas[mês] > média:
        print(f'{meses[mês]}: {temperaturas[mês]}')
