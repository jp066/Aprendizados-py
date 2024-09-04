#class Cachorro:
#    def __init__(self, nome, cor, acordado=True):
#        print('inicializando')
#        self.nome = nome
#        self.cor = cor
#        self.acordado = acordado
#        
#        
#    def __del__(self):
#        print('destruindo')    
#    
#    def latir(self):
#        print('auau')
#        
#        
#def criar():
#    c = Cachorro('rex', 'preto')
#    print('criando')
#    print(c.nome)
#        
#c = Cachorro('rex', 'preto')


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        print('inicializando')
        
    
    def criar(self):
        #nome = self.nome
        #print('criando')
        # mesma coisa que:
        print('criando')
        print(self.nome)
        
        
        
p1 = Pessoa('joao', 30)
p1.criar()