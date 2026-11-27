def filtrar_pares(lista_numeros):
    pares = []
    for numero in lista_numeros:
        if numero % 2 == 0:
            pares.append(numero)
    return pares
print(filtrar_pares([1, 2, 3, 4, 5, 6]))
print(filtrar_pares([10, 15, 20, 25, 30]))
print(filtrar_pares([1, 3, 5, 7]))
