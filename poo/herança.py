# classes multiplas herancas
class A:
    def __init__(self):
        self.variavel = 'variavel de A'
        
    def funcao(self):
        return self.variavel
    
class B:
    def __init__(self):
        self.variavel = 'variavel de B'
        
    def funcao(self):
        return self.variavel

class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        
    def funcao(self):
        return self.variavel
    
    def funcao_de_a(self):
        return A.funcao(self)
    
    
a_instancia = A()
print(a_instancia.funcao())  # Output: variavel de A

b_instancia = B()
print(b_instancia.funcao())  # Output: variavel de B

c_instancia = C()
print(c_instancia.funcao())  # Output: variavel de B
print(c_instancia.funcao_de_a())  # Output: variavel de A