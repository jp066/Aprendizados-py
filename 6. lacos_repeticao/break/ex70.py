# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# Crie um programa que leia o nome e o preço de vários produtos. 

# A) qual é o total gasto na compra.
# 
# B) quantos produtos custam mais de R$1000.
# 
# C) qual é o nome do produto mais barato.

print('cadastre um produto')

total = 0
mais_de_mil = 0
menor_preco = 0
nome_menor_preco = ' '
primeira_vez = True

while True:
    nome = str(input('digite o nome do produto: '))
    preco = float(input('digite o preco: '))
    total += preco
    if preco > 1000:
        mais_de_mil += 1
    if primeira_vez:
        menor_preco = preco
        nome_menor_preco = nome
        primeira_vez = False
    else:
        if preco < menor_preco:
            menor_preco = preco
            nome_menor_preco = nome
    continuar = ' '
    while continuar not in 'SimNao':
        continuar = str(input('deseja continuar? [Sim/Nao] ')).strip().capitalize()
        if not continuar in 'SimNao':
            print('opcao invalida. tente novamente')
    if continuar == 'Nao':
        break
print("-"*30)
print(f'o total gasto na compra foi de R${total}')
print(f'{mais_de_mil} produtos custam mais de R$1000')
print(f'o produto mais barato foi {nome_menor_preco} que custa R${menor_preco}')
print('fim do programa')
