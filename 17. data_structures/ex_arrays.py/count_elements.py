def contar_elementos(lista, elemento):
#   return lista.count(elemento)
    count = 0
    for item in lista:
        if item == elemento:
            count += 1
    return count


def contar_elementos_2(lista, elemento):
    return len([item for item in lista if item == elemento])


def contar_elementos_3(lista, elemento):
    return lista.count(elemento)



print(contar_elementos([1, 2, 3, 4, 5, 6, 3, 3], 3))
print(contar_elementos_2([1, 2, 3, 4, 5, 6, 3, 3], 3))
print(contar_elementos_3([1, 2, 3, 4, 5, 6, 3, 3], 3))