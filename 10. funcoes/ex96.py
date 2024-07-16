# Faça um programa que tenha uma função chamada área(), que receba 
# as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area(largura, comprimento):
    return largura * comprimento

largura = float(input('Largura do terreno: '))
comprimento = float(input('Comprimento do terreno: '))
print(f'A área do terreno é {area(largura, comprimento)} m²')