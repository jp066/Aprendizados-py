# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
num = int(input('digite um numero: '))
total = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print(f'{c}')
print(f'o numero {num} foi divisivel {total} vezes.')
if total == 2:
    print('por isso ele é primo.')
else:
        print('por isso ele não é primo.')