def encontrar_maior(lista):
    maior = lista[0]
    for num in lista:
        if num > maior:
            maior = num
    return maior


print(encontrar_maior([1, 2, 3, 4, 5]))