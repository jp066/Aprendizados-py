# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
# a soma entre todos os valores pares sorteados pela função anterior.
from random import randint


numeros = []

def sorteia():
    for inicio in range(5):
        numeros.append(randint(1, 10))
    print(f'Os números sorteados foram: {numeros}')
    
def somaPar():
    soma = 0
    for numero in numeros:
        if numero % 2 == 0:
            soma += numero
    print(f'A soma dos números pares é {soma}')

sorteia()
somaPar()