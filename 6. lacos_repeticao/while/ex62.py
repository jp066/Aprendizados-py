# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
# O programa encerrará quando ele disser que quer mostrar 0 termos.

print('Gerador de PA')
print('-='*10)

primeiro = int(input('primeiro termo: '))
razao = int(input('razão:'))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados')
print('FIM')