# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

lista = []

for vez in range(0,5):
    num = int(input('digite um numero: '))
    if vez == 0 or num > lista[-1]:
        lista.append(num)
        print('adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'adicionado na posicao {pos} da lista')
                break
            pos += 1
print(f'os valores digitados em ordem foram {lista}')