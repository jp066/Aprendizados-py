# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que 
# consiga mostrar os números como um valor monetário formatado.

from funcoes import aumentar_moeda, dobrar_moeda, metade_moeda, diminuir_moeda, moeda, ler_dinheiro


valor = ler_dinheiro(valor=0)
taxa = float(input('Digite a taxa de aumento: '))

print(f'Aumentando {taxa}% de R${moeda(valor)} temos R${moeda(aumentar_moeda(valor, taxa))}')
print(f'o dobro de {moeda(valor)} é R${moeda(dobrar_moeda(valor))}')
print(f'a metade de R${moeda(valor)} é R${moeda(metade_moeda(valor))}')
print(f'a diminuição de {taxa}% de R${moeda(valor)} temos R${moeda(diminuir_moeda(valor, taxa))}')
