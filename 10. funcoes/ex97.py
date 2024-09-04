# Faça um programa que tenha uma função chamada escreva(), 
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável. 

def escreva(texto):
    tamanho = len(texto) + 4
    print('-' * len(texto))
    print(texto)
    print('-' * len(texto))
    

texto = str(input('Digite um texto: '))
escreva(texto)