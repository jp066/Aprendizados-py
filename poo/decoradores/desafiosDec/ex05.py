def verificar_tipos(*tipos): #1
    def decorador(funcao): #2
        def wrapper(*args): #3
            for a, t in zip(args, tipos): # zip junta os elementos de args e tipos
                if not isinstance(a, t): # verifica se a é do tipo t
                    raise TypeError(f'Parâmetro {a} não é do tipo {t}')
            return funcao(*args) # 3
        return wrapper # 2
    return decorador # 1
# de 1 a 3 é a ordem de entrada de funções
# de 3 a 1 é a ordem de saída de funções
# ou seja, um decorador é uma função que retorna outra função que retorna outra função, em ordem inversa a de entrada.

@verificar_tipos(int, int)
def soma(a, b):
    return a + b

print(soma(1, 2)) # 3
print(soma(1, 'a')) # TypeError: Parâmetro a não é do tipo <class 'int'>