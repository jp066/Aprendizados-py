# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que 
# consiga mostrar os números como um valor monetário formatado.

from funcoes import aumentar_moeda, dobrar_moeda, metade_moeda, diminuir_moeda, moeda

valor = float(input('Digite o preço: R$'))

taxa = float(input('Digite a taxa de aumento: '))

print(f'Aumentando {taxa}% de R${moeda(valor)} temos R${moeda(aumentar_moeda(valor, taxa))}')
print(f'o dobro de {moeda(valor)} é R${moeda(dobrar_moeda(valor))}')
print(f'a metade de R${moeda(valor)} é R${moeda(metade_moeda(valor))}')
print(f'a diminuição de {taxa}% de R${moeda(valor)} temos R${moeda(diminuir_moeda(valor, taxa))}')
print(f'''
      resumo:
      valor => {moeda(valor)}
      aumento de {taxa} => {aumentar_moeda(valor, taxa)}
      redução de {taxa} => {diminuir_moeda(valor, taxa)}
      dobro => {dobrar_moeda(valor)}
      metade => {metade_moeda(valor)}''')