class ReversedListIterator:
    def __init__(self, lst):
        # O método __init__ é o construtor da classe. Ele inicializa a lista e o índice.
        self.lst = lst
        self.index = len(lst)  # O índice começa no tamanho da lista, indicando o final da lista.
        
    def __iter__(self):
        # O método __iter__ retorna o próprio objeto iterador, que é um iterável. nesse caso ele transforma a classe em um iterável.
        # Isso permite que o iterador seja usado em um laço for, por exemplo. e passa para o método __next__.
        return self
    
    def __next__(self):
        # O método __next__ é chamado para obter o próximo item do iterador.
        self.index -= 1  # Decrementa o índice para apontar para o próximo item na ordem reversa.
        if self.index >= 0:
            # Se o índice ainda está dentro dos limites da lista, retorna o item correspondente.
            return self.lst[self.index]
        # Se o índice está fora dos limites, levanta a exceção StopIteration para indicar o fim da iteração.
        raise StopIteration()
    
# Exemplo de uso do iterador ReversedListIterator
lst = [1, 2, 3, 4, 5]
# Cria uma instância do iterador e itera sobre os itens da lista em ordem reversa.
for item in ReversedListIterator(lst):
    print(item)