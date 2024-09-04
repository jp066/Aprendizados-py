def remover_elementos(lista, elemento):
    count = 0
    for item in lista:
        if item == elemento:
            count += 1
        if count > 0:
            lista.remove(elemento)
    return count


print(remover_elementos([1, 2, 3, 4, 5, 6, 3, 3], 3))