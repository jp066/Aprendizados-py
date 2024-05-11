# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, 
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('escreva uma frase: ')).strip()

print(frase)
print(f'a letra A aparece: {frase.count('a')} vezes')
#print(f'sua posicao inicial é {frase[:3].find('a')} e a posicao final é {frase[4:21].find('a')}')
print(f'a sua posição inicial é: {frase.find('a')+1}')
print(f'a sua posição final é: {frase.rfind('a')+1}')