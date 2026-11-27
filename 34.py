def avaliar_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7.0:
        situacao = "Aprovado"
    elif media >= 5.0:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
    return f"Média: {media:.2f} - {situacao}"
print(avaliar_media(8, 7, 9))
print(avaliar_media(5, 6, 6))
print(avaliar_media(3, 4, 2))
