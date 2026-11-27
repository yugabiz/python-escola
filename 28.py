def saudar(pessoa, horario='dia'):
    if horario == "dia":
        print(f'Bom dia, {pessoa}!')
    elif horario == 'tarde':
        print(f'Boa tarde, {pessoa}!')
    elif horario == 'noite':
        print(f'Boa noite, {pessoa}!')
saudar('Gabrielle')
saudar('James', 'tarde')
saudar('Ana', 'noite')
