'''Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única 
que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''

lista = [[], []]
for iterar in range(1,8):
    valor = int(input(f'digite um valor {iterar}: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print(f'os valores pares digitados foram: {lista[0]}')
print(f'os valores ímpares digitados foram: {lista[1]}')