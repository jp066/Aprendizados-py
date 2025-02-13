# Deque implementaion in python

class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addRear(self, item):
        self.items.append(item)

    def addFront(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop(0)

    def removeRear(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


mostragem = Deque()
print(mostragem.isEmpty())
mostragem.addRear(8)
mostragem.addRear(5)
mostragem.addFront(7)
mostragem.addFront(10)
print(mostragem.size())
print(mostragem.isEmpty())
mostragem.addRear(11)
print(mostragem.removeRear())
print(mostragem.removeFront())
mostragem.addFront(55)
mostragem.addRear(45)
print(mostragem.items)