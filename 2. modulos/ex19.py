from random import shuffle
a1 = str(input('digite um aluno: '))
a2 = str(input('digite um aluno: '))
a3 = str(input('digite um aluno: '))
a4 = str(input('digite um aluno: '))

lista = [a1, a2, a3, a4]

shuffle(lista)

print(f'a ordem de apresentação sera: {lista}')