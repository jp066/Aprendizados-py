from node import Node

class linkedList:
    # __init__ é como um construtor em flutter. this{} em dart
    # self: É uma referência ao próprio objeto dentro de uma classe ou método.
    def __init__(self):
        self.head = None
        self._size = 0
    
    def append(self, elem):
        
        if self.head:
            pointer = self.head # ponteiro para percorrer a lista, uma variavel auxiliar
            while(pointer.next): # enquanto o ponteiro não for o ultimo elemento
                pointer = pointer.next # o ponteiro vai para o proximo elemento
            pointer.next = Node(elem) # aqui o ultimo elemento recebe o novo elemento
        else:
            # 1 inserção
            self.head = Node(elem) # se a lista estiver vazia, o primeiro elemento é o novo elemento
        self._size += 1 # incrementa o tamanho da lista
        
        
    def __len__(self): # 
        return self._size
            
            
    def get(self, index):
        pass # pass é literalmente vazio, não faz nada
    
    
    def set(self, index, elem):
        pass
    
    
    def __getitem__(self, index):
        pointer = self.head # o self.head indica que o ponteiro começa no primeiro elemento da lista
        
        for i in range(index): # percorre a lista até o index desejado
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
            
        if pointer:
            return pointer.data 
        raise IndexError("list index out of range") # se o index não for encontrado, retorna um erro
    
    
    def __setitem__(self, index, elem):
        pointer = self.head
        
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
            
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("list index out of range")    
            
            
    def index(self, elem):
        pointer = self.head
        idx = 0
        while(pointer):
            if pointer.data == elem:
                return idx
            pointer = pointer.next
            idx += 1
        raise ValueError(f"{(elem)} is not in list")
        
lista = linkedList()
lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)
lista.append(5)

print(len(lista))
print(lista[1])
print(lista.index(5))