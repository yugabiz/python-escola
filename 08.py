# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).

fahrenheit = float(input("Temperatura em graus Fahrenheit: "))
graus_celsius = 5 * ((fahrenheit-32)/9)
print("Em graus Celsius",graus_celsius)
