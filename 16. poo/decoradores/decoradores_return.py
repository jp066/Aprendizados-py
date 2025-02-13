import functools
# o functools.wraps(funcao) é para manter o nome da função, como se fosse a função original.

def meu_decorador(funcao):
    @functools.wraps(funcao) # para manter o nome da função
    def envelope(*args, **kwargs):
        funcao(*args, **kwargs)
        
    return envelope


@meu_decorador
def minha_funcao(nome, numero):
    print(f'Minha função {nome}')
    return nome.upper()
    

print(minha_funcao.__name__)