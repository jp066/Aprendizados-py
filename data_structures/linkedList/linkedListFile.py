from node import Node

#sequencial  = []
##sequencial.append(1)
#sequencial.append(2)

class linkedList:
    def __init__(self):
        self.head = None
        self._size = 0
    
    def append(self, elem):
        
        if self.head:
            pointer = self.head
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
        else:
            # 1 inserção
            self.head = Node(elem)
        self._size += 1
        
        
    def __len__(self):
        return self._size
            
            
    def get(self, index):
        pass
    
    
    def set(self, index, elem):
        pass
    
    
    def __getitem__(self, index):
        pointer = self.head
        
        for i in range(index):
            if pointer:
                pointer = pointer.next
                
    
    
    def __setitem__(self, index, elem):
        pass
    
            
lista = linkedList()
lista.append(1)
lista.append(2)
lista.append(3)
lista.append(4)

print(lista._size)