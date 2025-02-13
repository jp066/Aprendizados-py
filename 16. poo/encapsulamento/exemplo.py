class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
        
    @property
    def nome(self):
        return self._nome
    
    
    @property
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self._idade
    
    
p1 = Pessoa('João', 30)
print(p1.nome)
print(p1.idade)