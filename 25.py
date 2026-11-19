semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']
somaTemperatura = 0
temperaturas = []
print('Estatísticas de Temperaturas')
for temperatura in range(7):
    temperatura = float(input(f'{semana[temperatura]}: '))
    somaTemperatura += temperatura
    temperaturas.append(temperatura)
print(f'TEMPERATURAS REGISTRADAS')
print(f'{temperaturas}')
média = somaTemperatura / 7
maior_temperatura = max(temperaturas)
menor_temperautura = min(temperaturas)
print(f'Média das temperaturas: {média:.1f}°')
print(f'Maior temperatura: {maior_temperatura}°')
print(f'Menor temperatura registrada: {menor_temperautura}°')
