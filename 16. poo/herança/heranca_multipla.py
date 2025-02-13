class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas
        
    
    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{k} = {v}' for k, v in self.__dict__.items()])}' # __class__ é um atributo que retorna a classe do objeto
    # __dict__ é um atributo que retorna um dicionário com os atributos do objeto
    # __name__ é um atributo que retorna o nome da classe
    # k é key e v é value
    
            
class Mamifero(Animal):
    def __init__(self, cor_pelos, **kw):
        self.cor_pelos = cor_pelos
        super().__init__(**kw)
        # quando kw for chamado, usa o valor do atributo nro_patas da classe pai.
    
class Ave(Animal):
    def __init__(self,cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)
        
        
    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{k} = {v}' for k, v in self.__dict__.items()])}' # __class__ é um atributo que retorna a classe do objeto
    
class Cachorro(Mamifero):
    pass
    
    
class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelos, nro_patas):
#        print(Ornitorrinco.__mro__)
        super().__init__(
            cor_bico=cor_bico, 
            cor_pelos=cor_pelos, 
            nro_patas=nro_patas
            )
        # nesse caso, o valor de nro_patas é passado para a classe pai, 
        # e o valor de cor_pelos e cor_bico é passado para a classe filha.
        # isso é feito para que o python saiba qual valor passar para cada classe.
        # pois se passarmos o valor de nro_patas para a classe filha, o python não saberá qual valor usar.
        # faz parte do method resolution order (MRO) do python.


cachorro = Cachorro(nro_patas=4, cor_pelos='marrom')
#print(cachorro)

orni = Ornitorrinco(nro_patas=4, cor_pelos='marrom', cor_bico='preto')
# orni recebe o valor de nro_patas da classe pai(animal), e o valor de cor_pelos e cor_bico da classe filha (mamifero e ave).
# agora os argumentos so podem ser passados de forma nomeada, pois a ordem dos argumentos não importa.
# nao podemos passar dois valores para o mesmo atributo, pois o python não sabe qual valor usar. portanto devemos passar
# um valor para cada atributo. e apagar o valor do atributo que não queremos passar 
# (no caso, o valor do atributo nro_patas que é da classe pai).
# para isso pasamos o valor da classe neta, e passamos o valor da classe pai como um **kwargs. 
# pois assim o python sabe que o valor passado é para a classe pai.
print(orni)