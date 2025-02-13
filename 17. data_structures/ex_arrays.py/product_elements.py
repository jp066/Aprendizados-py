def produto_elementos(lista):
    produto = 1
    for item in lista:
        produto *= item
    return produto


print(produto_elementos([1, 2, 3, 4, 5, 6, 3, 3]))