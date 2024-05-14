# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo.

while True:
    num = int(input('digite um numero: '))
    if num < 0:
        break
    for tabuada in range(1,11):
        print(f'{num} x {tabuada} = {tabuada * num}')
print('fim do programa')