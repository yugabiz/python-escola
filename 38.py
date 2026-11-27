def somar(valor1, valor2):
    return valor1 + valor2
def subtrair(valor1, valor2):
    return valor1 - valor2
def multiplicar(valor1, valor2):
    return valor1 * valor2
def dividir(valor1, valor2):
    if valor2 == 0:
        return 'Não é possível dividir por zero!'
    else:
        return valor1 / valor2
def executar_operacao(numero1, numero2, operacao):
    return operacao(numero1, numero2)
print(executar_operacao(10, 5, somar))
print(executar_operacao(10, 5, subtrair))
print(executar_operacao(10, 5, multiplicar))
print(executar_operacao(10, 5, dividir))
print(executar_operacao(10, 0, dividir))
