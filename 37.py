# Essa variável foi criada fora da função,
# por isso é considerada uma variável global.
curso = 'Desenvolvimento de Sistemas'
def apresentar():
    # Essa variável nasceu dentro da função,
    # então só conseguimos utilizá-la aqui dentro.
    materia = 'Lógica de Programação'
    print(f'Curso: {curso}')
    print(f'Matéria: {materia}')
apresentar()
# Aqui conseguimos mostrar o curso novamente,
# mas não conseguimos chamar a variável materia,
# porque ela pertence somente à função.
print(curso)
