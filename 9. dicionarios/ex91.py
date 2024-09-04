from random import randint

'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário em Python. No final, coloque esse dicionário em ordem, 
sabendo que o vencedor tirou o maior número no dado.'''

jogadores = {}
for jogador in range(1, 5):
    jogadores[f'jogador {jogador}'] = randint(1, 6)
print('Valores sorteados:')
for jogador, valor in jogadores.items():
    print(f'{jogador} tirou {valor} no dado.')
print('Ranking dos jogadores:')
for indice, jogador in enumerate(sorted(jogadores, key=jogadores.get, reverse=True)):
    print(f'{indice+1}º lugar: {jogador} com {jogadores[jogador]}')