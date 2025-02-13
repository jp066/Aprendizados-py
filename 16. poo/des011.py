class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        # o metodo __init__ é um método especial que é chamado quando um objeto é instanciado.
        # o self é uma referência ao objeto que está sendo instanciado.
        
    
    def buzinar(self):
        print('bibibi')
    # o método buzinar é uma ação que a bicicleta pode fazer. o argumento self é obrigatório.
        
        
    def pedalar(self):
        print('pedalando')
        
    
    def __str__(self):
        return f'{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor 
        in self.__dict__.items()])}'
    
    
bicicleta_1 = Bicicleta('vermelha', 'caloi', 2020, 500.00)
bicicleta_1.buzinar()
bicicleta_1.pedalar()
print(bicicleta_1.cor)

bicicleta_1

print(bicicleta_1)