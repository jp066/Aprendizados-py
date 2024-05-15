# Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# 
# A) quantas pessoas tem mais de 18 anos.
# 
# B) quantos homens foram cadastrados.
# 
# C) quantas mulheres tem menos de 20 anos.

print('cadastre uma pessoa')
idade = 0
sexo = ' '
maior_idade = 0
homens = 0
mulheres = 0
while True:
    idade = int(input('digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('digite o sexo [M/F]:')).strip().upper()[0]
        if not sexo in 'MF':
            print('opcao invalida. tente novamente')
    if idade > 18:
        maior_idade += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    continuar = ' '
    while continuar not in "SN":
        continuar = str(input('deseja continuar? [S/N]')).strip().upper()[0]
        if not continuar in 'SN':
            print('opcao invalida. tente novamente')
    if continuar == 'N':
        break
print(f'{maior_idade} pessoas tem mais de 18 anos')
print(f'{homens} homens foram cadastrados')
print(f'{mulheres} mulheres tem menos de 20 anos')
print('fim do programa')        