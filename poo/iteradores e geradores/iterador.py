# numero contável de valores que podem ser iterados, pode percorrer os valores de um objeto.
# iterador é um objeto que implementa o método __next__(), que acessa os elementos de uma coleção um de cada vez.
# ou __iter__() que retorna um iterador.
# usado para economizar memória, pois não armazena todos os valores na memória, apenas um de cada vez.

class MeuIterador:
    
    def __init__(self, x: list[int]):
        self.x = x
        self.contador = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            numero = self.x[self.contador]
            self.contador += 1
            return  numero * 2
        except IndexError:
            raise StopIteration


for i in MeuIterador(x=[10, 20, 30, 40, 50]):
    print(i)