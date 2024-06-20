'''Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.'''

matriz = [[0,0,0], [0,0,0], [0,0,0]]
soma_pares = 0

for linha in range (0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'digite um valor para [{linha}, {coluna}]: '))
print('-='*30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
    
for linha in range(0, 3):
    for coluna in range(0, 3):
        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
print(f'a soma dos valores pares é {soma_pares}')

soma_terceira_coluna = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'a soma dos valores da terceira coluna é {soma_terceira_coluna}')

maior_valor_segunda_linha = max(matriz[1])
print(f'o maior valor da segunda linha é {maior_valor_segunda_linha}')