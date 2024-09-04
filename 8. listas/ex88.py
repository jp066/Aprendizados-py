'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e 
vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''

from random import randint

jogos = []
jogo = []

aposta = int(input('quantos jogos você quer que eu sorteie? '))

for iterar in range(0, aposta):
    for jogosSorteados in range(0,6):
        jogo.append(randint(1,60))
    jogos.append(jogo[:])
    jogo.clear()
print(f'os jogos sorteados foram: {jogos}')

print('-='*30)

for indice, jogo in enumerate(jogos):
    print(f'jogo {indice+1}: {jogo}')
print('-='*30)
print('boa sorte!')