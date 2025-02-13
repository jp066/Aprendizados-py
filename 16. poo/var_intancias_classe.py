# aprendendo variaveis de instancia e classe

class Carro:
    def __init__(self, modelo, marca, ano):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        # variavel de instancia é uma variavel que pertence a um objeto.
        # ou seja, cada objeto tem sua propria copia da variavel.
        # é como se fosse uma referencia para o objeto.
        

carro1 = Carro('fiesta', 'ford', 2019) # carro1 é um objeto
print(carro1.modelo)


class Carro:
    rodas = 4
    def __init__(self, modelo, marca, ano):
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        # o que diferencia uma variavel de instancia de uma variavel de classe
        # é que a variavel de classe é compartilhada por todos os objetos da classe.
        # ou seja, a variavel de classe é uma variavel que pertence a classe.