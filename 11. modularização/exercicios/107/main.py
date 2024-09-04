# Crie um módulo chamado moeda.py que tenha as funções incorporadas 
# aumentar(), diminuir(), dobro() e metade(). 
# Faça também um programa que importe esse módulo e use algumas dessas funções.

from funcoes import aumentar_moeda, dobrar_moeda, metade_moeda, diminuir_moeda

valor = float(input('Digite o preço: R$'))
taxa = float(input('Digite a taxa de aumento: '))

print(f'Aumentando {taxa}% de R${valor} temos R${aumentar_moeda(valor, taxa)}')
print(f'o dobro de R${valor} é R${dobrar_moeda(valor)}')
print(f'a diminuição de {taxa}% de R${valor} temos R${diminuir_moeda(valor, taxa)}')
print(f'a metade de R${valor} é R${metade_moeda(valor)}')