# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
print('\n')
palavra1 = str(input('Digite uma palavra: '))
palavra2 = str(input('Digite uma palavra: '))
palavra3 = str(input('Digite uma palavra: '))
palavra4 = str(input('Digite uma palavra: '))
palavra5 = str(input('Digite uma palavra: '))
palavra6 = str(input('Digite uma palavra: '))

palavras = (palavra1, palavra2, palavra3, palavra4, palavra5, palavra6)
print('-'*50)

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')