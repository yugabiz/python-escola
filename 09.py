# Faça um algoritmo que leia um número N e imprima “F1” se N for menor ou igual a 10, “F2” se N for maior que 10 e menor ou igual a 100, ou “F3” se N for maior que 100.

n = int(input('Digite um número: '))
if(n <= 10):
    print('F1')
elif(n > 10 and n <= 100):
    print('F2')
else:
    print('F3')
