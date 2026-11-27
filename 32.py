def contar_vogais(frase):
    contador = 0
    for letra in frase:
        if letra.lower() in 'aeiou':
            contador += 1
    return contador
print(contar_vogais('Marcos'))
print(contar_vogais('Desenvolvimento1'))
print(contar_vogais('Python'))
