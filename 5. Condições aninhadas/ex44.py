from math import trunc
preco_produto = float(input('digite o preço do produto que você vai querer: '))
pagamento = int(input('''digite a condição do pagamento: 
1. à vista dinheiro/cheque: 10"%" de desconto 
2. à vista no cartão: 5"%" de desconto
3. em até 2x no cartão: preço formal
4. 3x ou mais no cartão: 20"%" de juros
: '''))

if (pagamento == 1):
    pagamento = 'à vista dinheiro/cheque'
    desconto = 0.10 * preco_produto
    valor_final = preco_produto + desconto
    print(f'o produto que era {preco_produto} agora fica {valor_final} reais com {pagamento}')

elif (pagamento == 2):
    pagamento = 'à vista no cartão: 5"%" de desconto'
    desconto = 0.05 * preco_produto
    valor_final = preco_produto + desconto
    print(f'o produto que era {preco_produto} agora fica {valor_final} reais com {pagamento}')

elif (pagamento == 3):
    pagamento = 'em até 2x no cartão: preço formal'
    valor_final = preco_produto / 2
    print(f'o produto que era {preco_produto} agora fica {valor_final} reais, {pagamento}')

elif (pagamento == 4):
    pagamento = '3x ou mais no cartão: 20"%" de juros'
    parcelas = int(input('''quantas parcelas? 
3. 3x
4. 4x
5. 5x
6. 6x
7. 7x
: '''))
    valor_parc = preco_produto + (preco_produto * 0.20)
    valor_final = valor_parc / parcelas
    print(f'o produto que era {preco_produto} agora sera {valor_final} em {trunc(parcelas)} meses, com {pagamento}')