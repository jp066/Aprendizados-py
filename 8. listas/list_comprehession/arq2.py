# [expression for item in list if condition] 
# expression: o que será retornado, ou seja, o que será adicionado a lista.

precos = [4.5, 7.8, 6, 2.9]
precosComAumento = [preco *1.1 for preco in precos]
print(precosComAumento)  # [4.95, 8.58, 6.6, 3.19]