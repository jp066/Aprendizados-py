def somar_elementos(lista):
    soma = 0
    for num in lista:
        soma += num
    return soma

lista = [1, 2, 3, 4, 5]

print(somar_elementos(lista))