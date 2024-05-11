# Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

num = 0
cont = 0
soma = 0

while True:
    num = int(input('digite um numero: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == "N":
        break
media = soma / cont
print(f'Você digitou {cont} números e a média entre eles é {media}')