class Foo:
    def __init__(self, x=None):
        self._x = x
        
    @property
    def x(self):
        return self._x or 0
    # O método getter é chamado quando o atributo é acessado

    @x.setter
    def x(self, value):
        return self._x + value
    # O método setter é chamado quando o atributo é modificado
    
    @x.deleter
    def x(self):
        self._x = -1
    
f = Foo(10)
print(f.x)  # 10
f.x = 20
print(f.x)  # 30
del f.x
print(f.x)  # 0