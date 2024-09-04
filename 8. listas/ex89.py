'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''

alunos = []
aluno = []
notas = []
nota = []

while True:
    aluno.append(str(input('nome do aluno: ')))
    nota.append(float(input('nota 1: ')))
    nota.append(float(input('nota 2: ')))
    aluno.append(nota[:])
    notas.clear()
    alunos.append(aluno[:])
    aluno.clear()
    continuar = str(input('quer continuar? [s/n] '))
    if continuar in 'nN':
        break
    
print('-='*30)

print(f'{"nº":<4}{"|nome":<10}{"|média":>8}')
print('-'*22)
for indice, aluno in enumerate(alunos):
    media = (aluno[1][0] + aluno[1][1]) / 2
    print(f'{indice:<4}|{aluno[0]:<10}|{media:>8.1f}')
print('-='*30)

while True:
    verifica = str(input('quer ver as notas de algum aluno? [s/n] '))
    if verifica in 'nN':
        break
    mostrar = int(input('digite a matricula do aluno (999 interrompe) '))
    print(f'as notas de {alunos[mostrar][0]} são {alunos[mostrar][1]}')
    print('-='*30)
print('fim do programa')
print("-"*50)