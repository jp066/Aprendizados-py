def uppercas_decorator(function):
    def wrapper():
        func = function() # recebe e faz um objeto da função inicial
        make_uppercase = func.upper() # deixa em maiúsculo
        return make_uppercase # retorna o resultado
    return wrapper # retorna o decorador com o nome de @uppercas_decorator


def split_string(function):
    def wrapper():
        func = function()
        splitted = func.split()
        return splitted
    return wrapper

@uppercas_decorator
@split_string
def text():
    return 'hello world'

print(text())