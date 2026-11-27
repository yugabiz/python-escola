def somar_todos(*numeros):
    soma = 0
    for valor in numeros:
        soma += valor
    return soma
print(somar_todos(2, 3))
print(somar_todos(5, 10, 15))
print(somar_todos(1, 2, 3, 4, 5))
print(somar_todos())
