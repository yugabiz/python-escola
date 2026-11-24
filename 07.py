# Crie um script que leia um número e mostre na tela sua tabuada.

num = int(input("Digite um número: "))
print("\nTABUADA DO",num,":")
for i in range(0,11):
    resultado = num * i
    print(num,"x",i,"=",resultado)
    
