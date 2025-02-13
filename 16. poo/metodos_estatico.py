class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    @classmethod
    def metodo_classe(cls, nome, ano_nascimento):
        idade = 2021 - ano_nascimento
        return cls(nome, idade)
    
    @staticmethod
    def metodo_estatico(idade):
        return idade >= 18
    
p = Pessoa.metodo_classe('Lucas', 1995)
print(p.nome, p.idade)
print(Pessoa.metodo_estatico(18))
print(Pessoa.metodo_estatico(17))