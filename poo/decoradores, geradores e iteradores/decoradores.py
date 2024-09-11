def meu_decorador(funcao):
    def envelope():
        print('Antes da função')
        funcao()
        print('Depois da função')
        
    return envelope

@meu_decorador
def minha_funcao():
    print('Minha função')
    
    
minha_funcao()
# funcao = meu_decorador(minha_funcao)
# açucar sintático
# @meu_decorador