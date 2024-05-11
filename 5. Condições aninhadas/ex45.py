from random import randint

itens = ('pedra', 'papel', 'tesoura')

computador = randint(0,2)
usuario = int(input('''escolha sua jogada:
[0] pedra
[1] papel
[2] tesoura
=> '''))

if (usuario == 0 and computador == 0 or usuario == 1 and (computador) == 1 or usuario == 2 and (computador) == 2):
    print(f'deu empate!, com usuario {itens[usuario]} e computador {itens[computador]}')

elif (usuario == 0 and computador == 2 or usuario == 2 and computador == 1 or usuario == 1 and computador == 0):
    print(f'o usuario venceu, {itens[usuario]} ganha de {itens[computador]}')

elif (computador == 0 and usuario == 2 or computador == 2 and usuario == 1 or computador == 1 and usuario == 0):
    print(f'o computador venceu, {itens[usuario]} perde de {itens[computador]}')
