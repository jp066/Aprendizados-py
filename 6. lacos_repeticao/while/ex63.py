# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
# Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

num = int(input('digite um número: '))
cont = 0
a = 0
b = 1
print(f'{a} -> {b}', end='')
while cont < num - 2:
    c = a + b
    print(f' -> {c}', end='')
    a = b 
    b = c
    cont += 1
print(' -> FIM')
