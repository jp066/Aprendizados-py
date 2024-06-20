# Faça um programa que leia nome e peso de várias pessoas,
# guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

temporaria = []
principal = []
maior = menor = 0
while True:
    temporaria.append(str(input('nome: ')))
    temporaria.append(float(input('peso: ')))
    if len(principal) == 0:
        maior = menor = temporaria[1]
    else:
        if temporaria[1] > maior:
            maior = temporaria[1]
        if temporaria[1] < menor:
            menor = temporaria[1]
    principal.append(temporaria[:])
    temporaria.clear()
    resp = str(input('quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
    else:
        continue
print(f'foram cadastradas {len(principal)} pessoas')
print(f'o maior peso foi de {maior}kg.')

for pessoa in principal:
    if pessoa[1] == maior:
        print(f'{pessoa[0]} tem o maior peso.')
    elif pessoa[1] == menor:
        print(f'{pessoa[0]} tem o menor peso.')

print(f'o menor peso foi de {menor}kg.')