# Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint

vitorias = 0
while True:
    jogador = int(input('digite um numero: '))
    computador = randint(0,10)
    total = jogador + computador
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('par ou impar? [P/I] ')).strip().upper()[0]
        if not escolha in 'PI':
            print('opcao invalida. tente novamente')
        else:
            print(f'voce jogou {jogador} e o computador {computador}. total de {total}', end=' ')
            print('deu par' if total % 2 == 0 else 'deu impar')
    if escolha == 'P':
        if total % 2 == 0:
            print('voce venceu')
            vitorias += 1
        else:
            print('voce perdeu')
            break
    elif escolha == 'I':
        if total % 2 == 1:
            print('voce venceu')
            vitorias += 1
        else:
            print('voce perdeu')
            break
    print('vamos jogar novamente...')
print(f'voce venceu {vitorias} vezes')
print('fim do programa')