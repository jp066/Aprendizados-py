def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print('Antes da função')
        funcao(*args, **kwargs)
        print('Depois da função')
        return funcao(*args, **kwargs)
        
    return envelope

@meu_decorador
def minha_funcao(nome):
    print(f'Minha função{nome}')
    
    
minha_funcao('joao')