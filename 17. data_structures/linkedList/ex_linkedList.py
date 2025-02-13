class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        return
    
    
    def print_list(self):
        if self.head == None:
            return 0
        cur_node = self.head
        total = 0
        
        while cur_node:
            total += 1
            cur_node = cur_node.next
        return total
    
    
    def to_list(self):
        node_data = []
        current_node = self.head

        while current_node:
            node_data.append(current_node.data)
            current_node = current_node.next
        return node_data
    

    def search(self, target):
        current_node = self.head

        while current_node:
            if current_node.data == target:
                return True
            current_node = current_node.next
        return False


    def display(self):
        contents = self.head

        if contents is None:
            print("List is empty")

        while contents:
            print(contents.data)
            contents = contents.next
        print('----------------------------------------')
        print("End of list")


    def get(self, index):
        if index >= self.print_list():
            return None
        current_idx = 0
        current_node = self.head
        
        while current_node:
            if current_idx == index:
                return current_node.data
            current_node = current_node.next
            current_idx += 1
        return None

    def reverse_linked_list(self):
        prev_node = None
        current_node = self.head
        
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node
        
# testando funções
        
minha_lista = LinkedList()
minha_lista.append(1)
minha_lista.append(2)
minha_lista.append(3)
minha_lista.append(4)
minha_lista.append(5)
minha_lista.append(6)


print('total de comprimentos: ' + str(minha_lista.print_list()))
print(minha_lista.to_list())

minha_lista.reverse_linked_list()


minha_lista.get(2)  # Output: 3
minha_lista.search(3)  # Output: True


minha_lista.display()