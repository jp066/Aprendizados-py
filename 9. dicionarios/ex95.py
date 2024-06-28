# Aprimore o desafio 93 para que ele funcione com vários jogadores, 
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

jogadores = []

while True:
    nome_jogador = str(input('Nome do jogador: '))
    partidas = int(input('Quantas partidas ele jogou? '))
    gols = []
    for partida in range(1, partidas+1):
        gols.append(int(input(f'Quantos gols na partida {partida}? ')))
    total_gols = sum(gols)
    jogador = {'nome': nome_jogador, 'partidas': partidas, 'total de gols': total_gols, 'gols por partida': gols}
    print(f'O jogador {nome_jogador} jogou {partidas} partidas e fez um total de {total_gols} gols. tem uma média de {total_gols / partidas:.2f} gols por partida.')
    jogadores.append(jogador)
    
    opcao = str(input('Deseja continuar? [S/N]: '))
    if opcao in 'Nn':
        break
    else:
        continue
    

print('comparativos entre jogadores: ')
print('.' * len('comparativos entre jogadores: '))
for jogador in jogadores:
    print(f"Nome: {jogador['nome']}")
    print(f"Partidas: {jogador['partidas']}")
    print(f"Total de gols: {jogador['total de gols']}")
    print(f"Gols por partida: {jogador['gols por partida']}")
    print(f'Média de gols por partida: {jogador["total de gols"] / jogador["partidas"]:.2f}')
    print("-" * len(str(jogador)))