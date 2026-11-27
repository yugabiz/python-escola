def maior_de_tres(primeiro, segundo, terceiro):
    if primeiro > segundo and primeiro > terceiro:
        return primeiro
    elif segundo > primeiro and segundo > terceiro:
        return segundo
    else:
        return terceiro
print(maior_de_tres(10, 5, 8))
print(maior_de_tres(3, 15, 7))
print(maior_de_tres(4, 6, 20))
