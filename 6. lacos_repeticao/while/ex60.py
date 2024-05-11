# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 
# 5! = 5 x 4 x 3 x 2 x 1 = 120

num = int(input('digite um número: '))

fatorial = 1

print(f'{num}! = ', end='')

while num > 0:
    print(f'{num}', end='')
    print(' x ' if num > 1 else ' = ', end='')
    fatorial = fatorial * num
    num = num - 1
print(fatorial)