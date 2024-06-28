# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
# em um dicionário e todos os dicionários em uma lista. No final, mostre: 
# A) Quantas pessoas foram cadastradas 
# B) A média de idade 
# C) Uma lista com as mulheres 
# D) Uma lista de pessoas com idade acima da média


nome = str(input('Nome: '))
sexo = str(input('Sexo [M/F]: '))
idade = int(input('Idade: '))
pessoas = []

while True:
    dados = {'nome': nome, 'sexo': sexo, 'idade': idade}
    pessoas.append(dados)
    opcao = str(input('Deseja continuar? [S/N]: '))
    if opcao in 'Nn':
        break
    else:
        nome = str(input('Nome: '))
        sexo = str(input('Sexo [M/F]: '))
        idade = int(input('Idade: '))
    
print(f'Foram cadastradas {len(pessoas)} pessoas.')
soma_idade = 0
mulheres = []
acima_media = []
for pessoa in pessoas:
    soma_idade += pessoa['idade']
    if pessoa['sexo'] in 'Ff':
        mulheres.append(pessoa['nome'])
media_idade = soma_idade / len(pessoas)
print(f'A média de idade é {media_idade:.2f} anos.')
print(f'As mulheres cadastradas foram: {mulheres}')
print(f'Pessoas com idade acima da média: {acima_media}')

for pessoa in pessoas:
    if pessoa['idade'] > media_idade:
        acima_media.append(pessoa['nome'])