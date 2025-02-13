def busca_binaria(array, alvo):
    esquerda, direita = 0, len(array) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if array[meio] == alvo:
            return meio
        elif array[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1

    
# Exemplo de uso
array_ordenado = [1, 2, 3, 4, 5, 6, 7, 8, 9]
indice = busca_binaria(array_ordenado, 9)
print(indice)  # Output: 4