def meu_decorador(funcao):
    def wrapper():
        print('antes da função')
        funcao() # funcão que será recebida
        print('depois da função')
    return wrapper    
    