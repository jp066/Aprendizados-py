# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
for par in range(0,51):
    if not (par % 2):
        print(f'{par} é par')
print('acabou!')