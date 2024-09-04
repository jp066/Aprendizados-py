# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

produtos = ('shampoo', 10, 'condicionador', 12.00, 'mascara', 15.90, 'serúm', 25.00, 'spray', 4.20, 'kit de restauração capilar', 34.90)

print('-' * 40)
print('LISTAGEM DE PREÇOS')
print('-' * 40)

for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    else:
        print(f'R${produtos[pos]:>7.2f}')
print('-' * 40)