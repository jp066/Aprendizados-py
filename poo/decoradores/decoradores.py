#def meu_decorador(funcao):
#    def envelope():
#        print('Antes da função')
#        funcao()
#        print('Depois da função')
#        
#    return envelope
#
#@meu_decorador
#def minha_funcao():
#    print('Minha função')
#    
#    
#minha_funcao()
## funcao = meu_decorador(minha_funcao)
## açucar sintático
## @meu_decorador
#
#
def validar(funcao):
    def valida(x,y):
        if x < 0 or y < 0:
            raise ValueError ('Não pode ser negativo')
        x *= 2
        y *= 2
        return funcao(x,y)
    return valida

@validar # soma = validar(soma)
def soma(x,y):
    return x + y


print(soma(10,10))