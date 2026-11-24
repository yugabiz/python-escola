# Escreva em python um script que receba o ano atual, ano de nascimento de uma pessoa e mostre a sua idade.

ano_atual = int(input("Digite o ano atual: "))
ano_de_nascimento = int(input("Digite o ano de seu nascimento: "))
idade = ano_atual - ano_de_nascimento
print("Você tem",idade,"anos")
