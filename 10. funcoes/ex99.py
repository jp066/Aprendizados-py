# Faça um programa que tenha uma função chamada maiorNum(), que receba vários parâmetros com valores inteiros. 
# Seu programa tem que analisar todos os valores e dizer qual deles é o maiorNum.


def maiorNum(*numeros):
    if not numeros:
        print('Nenhum número foi informado.')
        return
    maiorNum = max(numeros)
    print(f'O maior número é {maiorNum}')
    
    
def mostrarNumeros(*numeros):
    if not numeros:
        print('Nenhum número foi informado.')
        return
    print('Os números informados foram: ')
    for numero in numeros:
        print(numero)
    
    
numerosDigitados = []
    
while True:
    numero = int(input('Digite um número (ou 0 para sair): '))
    if numero == 0:
        break
    numerosDigitados.append(numero)
    
maiorNum(*numerosDigitados)
mostrarNumeros(*numerosDigitados)