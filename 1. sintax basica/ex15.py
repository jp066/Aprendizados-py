# calcule a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km_percorrido = int(input('qual a qtd de km percorrido? '))
dias_alugado = int(input('qauntos dias de aluguel? '))

preco = (km_percorrido * 0.15) + (dias_alugado * 60)

print(preco)