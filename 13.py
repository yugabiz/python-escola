código = int(input('Digite o seu código de funcionário: '))
a_a = int(input('Digite o ano atual: '))
a_n = int(input('Digite o ano do seu nascimento: '))
a_e = int(input('Digite o ano de ingresso a empresa: '))
i = a_a - a_n
t_t = a_a - a_e
print(f'Você tem {i} anos')
print(f'O tempo trabalhado na empresa é de {t_t} ano(s)')
if i >= 65 or t_t >= 30 or i >= 60 and t_t >=25:
    print('Requer Aposentadoria')
else:
    print('Não Requer Aposentadoria')
