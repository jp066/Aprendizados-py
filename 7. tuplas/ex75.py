# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# 
# A) Quantas vezes apareceu o valor 9.
# 
# B) Em que posição foi digitado o primeiro valor 3.
# 
# C) Quais foram os números pares.

num = (int(input('Digite um número: ')))
num2 = (int(input('Digite um número: ')))
num3 = (int(input('Digite um número: ')))
num4 = (int(input('Digite um número: ')))

tupla = (num, num2, num3, num4)

print(f'O número 9 apareceu {tupla.count(9)} vezes.')

if 3 in tupla:
    print(f'O número 3 apareceu na posição {tupla.index(3)}')
else:
    print('O número 3 não foi digitado.')
    
print('Os números pares digitados foram: ', end='')
for num in tupla:
    if num % 2 == 0:
        print(num, end=' ')