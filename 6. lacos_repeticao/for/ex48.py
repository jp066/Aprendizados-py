# Faça um programa que calcule a soma entre todos os números que são múltiplos de três 
# e que se encontram no intervalo de 1 até 500.
soma = 0
for num in range(0,501):
    if num % 3 == 0:
        soma =+ num
        print(f'a soma de todos os numeros é {soma}')