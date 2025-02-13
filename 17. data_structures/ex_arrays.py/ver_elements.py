def verificar_elemento(lista, elemento):
    if elemento in lista:
        return 'Elemento encontrado'
    else:
        return 'Elemento não encontrado'


print(verificar_elemento([1, 2, 3, 4, 5], 6))