# Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
# Ao final, mostre o conteúdo das três listas geradas.

lista = []
pares = []
impares = []
# definindo 3 listas

while True:
    numero = int(input('digite um numero: '))
    lista.append(numero) # adicionando o numero na lista
    if numero % 2 == 0:
        pares.append(numero) # adicionando o numero na lista de pares
    else:
        impares.append(numero) # adicionando o numero na lista de impares
        
    continuar = str(input('quer continuar? [S/N] ')).strip().upper() # perguntando se quer continuar
    if continuar == 'N':
        break # se a resposta for N, o programa para
    else:
        continue # se a resposta for S, o programa continua

# exibindo
print(f'os numeros digitados foram {lista}')
print(f'os numeros pares sao {pares}')
print(f'os numeros impares sao {impares}')