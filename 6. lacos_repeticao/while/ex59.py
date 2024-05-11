#  Crie um programa que leia dois valores e mostre um menu na tela:
# 
# [ 1 ] somar
# 
# [ 2 ] multiplicar
# 
# [ 3 ] maior
# 
# [ 4 ] novos números
# 
# [ 5 ] sair do programa
# 
# Seu programa deverá realizar a operação solicitada em cada caso.

num1 = int(input('digite o primeiro número: '))
num2 = int(input('digite o segundo número: '))

opcao = 0

while opcao != 5:
    print('''
1. somar
2. multiplicar
3. maior
4. novos números
5. sair do programa''')
    opcao = int(input('qual sua opcao? '))
    if opcao == 1:
        print(f'{num1} + {num2} = {num1 + num2}')
    elif opcao == 2:
        print(f'{num1} x {num2} = {num1 * num2}')
    elif opcao == 3:
        print(f'o maior número é {max(num1, num2)}')
    elif opcao == 4:
        num1 = int(input('digite novamente o primeiro número:'))
        num2 = int(input('digite novamente o segundo número:'))
    elif opcao == 5:
        print('saindo do programa...')
    else:
        print('opção inválida. Tente novamente')