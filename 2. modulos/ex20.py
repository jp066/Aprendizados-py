import random
## Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
## Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

a1 = str(input('digite um aluno: '))
a2 = str(input('digite um aluno: '))
a3 = str(input('digite um aluno: '))
a4 = str(input('digite um aluno: '))

lista = [a1, a2, a3, a4]

nome_escolhido = random.choices(lista)

print(nome_escolhido)