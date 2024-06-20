# Crie um programa que vai ler vários números e colocar em uma lista.                  
# Depois disso, mostre: 
# A) Quantos números foram digitados. 
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.

lista = []

while True:
    numero = int(input('digite um numero: '))
    lista.append(numero)
    continuar = str(input('quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
    else:
        continue
print(f'voce digitou {len(lista)} numeros')
lista.sort(reverse=True)
print(f'os numeros digitados em ordem decrescente sao {lista}')
if 5 in lista:
    print('o numero 5 esta na lista')
else:
    print('o numero 5 nao esta na lista')