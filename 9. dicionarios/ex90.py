# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. 
# No final, mostre o conteúdo da estrutura na tela.

dicionario = {}
dicionario['nome'] = str(input('Nome: '))
dicionario['media'] = float(input(f'Média de {dicionario["nome"]}: '))
if dicionario['media'] >= 7:
    dicionario['situacao'] = 'Aprovado'
elif 5 <= dicionario['media'] < 7:
    dicionario['situacao'] = 'Recuperação'
else:
    dicionario['situacao'] = 'Reprovado'
print(f'{dicionario["nome"]} está {dicionario["situacao"]} com média {dicionario["media"]}')