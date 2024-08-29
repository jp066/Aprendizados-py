class Passaro:
    def voar(self):
        print('voar')
        

class Pardal(Passaro):
    def voar(self):
        return super().voar()
    
    
class Avestruz(Passaro):
    def voar(self):
        print('avestruz n voa')
        
        
def plano_voo(obj):
    obj.voar()
    

class Aviao(Passaro):
    def voar(self):
        print('o aviao esta decolando')

a1 = Aviao()
p1 =  Pardal()
p2 = Avestruz()

plano_voo(p1)
plano_voo(p2)
plano_voo(a1)

# polimorfismo é 