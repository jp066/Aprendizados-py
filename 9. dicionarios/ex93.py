# Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
# O programa vai ler o nome do jogador e quantas partidas ele jogou. 
# Depois vai ler a quantidade de gols feitos em cada partida. 
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.


jogadores = []

while True:
    nome_jogador = str(input('Nome do jogador: '))
    partidas = int(input('Quantas partidas ele jogou? '))
    gols = []
    for partida in range(1, partidas+1):
        gols.append(int(input(f'Quantos gols na partida {partida}? ')))
    total_gols = sum(gols)
    jogador = {'nome': nome_jogador, 'partidas': partidas, 'total de gols': total_gols}
    print(f'O jogador {nome_jogador} jogou {partidas} partidas e fez um total de {total_gols} gols.')
    jogadores.append(jogador)
    
    opcao = str(input('Deseja continuar? [S/N]: '))
    if opcao in 'Nn':
        break
    else:
        continue
    

print('comparativos entre jogadores: ')
print('.' * len('comparativos entre jogadores: '))
for jogador in jogadores:
    print(jogadores)
    print("-" * len(str(jogador)))