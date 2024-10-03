def cache(func):
    memoria = {}
    def cache_func(*args):
        if args in memoria:
            print(f'resultado em cache {args}')
            return memoria[args]
        resultado = func(*args) # é o resultado da função fatorial
        memoria[args] = resultado
        return resultado
    
    return cache_func


@cache # nessa linha a função fatorial é chamada pelo decorador cache, que modifica o comportamento da função fatorial, passando a ter comportamento de cache
def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n-1)


print(fatorial(7))
print(fatorial(8))
print(fatorial(7))