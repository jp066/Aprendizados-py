# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []

while True:
    n = int(input('digite um numero: '))
    if n not in lista:
        lista.append(n)
    else:
        print('numero ja existe')
    resp = str(input('quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
lista.sort()
print(f'voce digitou os numeros {lista}')