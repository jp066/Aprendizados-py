'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
    Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''
from random import randint

print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
compuntador = randint(0,10)
acertou = False
palpites = 0

while not acertou:
    jogador = int(input('qual seu palpite? '))
    palpites += 1
    if jogador == compuntador:
        acertou = True
    else:
        if jogador < compuntador:
            print('Mais... tente novamente')
        elif jogador > compuntador:
            print('Menos... tente novamente')
print(f'Acertou com {palpites} tentativas. Parabéns!')