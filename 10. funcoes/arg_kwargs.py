# args e kwargs são opcionais, ou seja, não precisamos passar argumentos para eles, mas se passarmos, args será uma tupla e kwargs será um dicionário.
# args - quando não sabemos quantos argumentos serão passados para a função.
# kwargs - quando não sabemos quantos argumentos nomeados serão passados para a função.

def sum(*args):
    total = 0
    for n in args:
        total += n
    return total

print(sum(7,4))

#em uma função, os argumentos são o que você passa para a função, e os parâmetros são o que você usa na função. ex:
def soma(a, b): # a e b são parâmetros
    return a + b # a e b são argumentos

# ou seja os parâmetros são as variáveis que você usa na função, e os argumentos são os valores que você passa para a função.
# basicamente, enquanto um recebe, o outro usa e finaliza a operação.


def presentation(**kwargs): # os argumentos nomeados são passados para a função como um dicionário
    for key, value in kwargs.items(): # o for key, value é usado para percorrer o dicionário, que é kwargs.items(), passado como argumento para a função.
        print(f'{key} is {value}')
print("Lista de cursos:")
presentation(curso1='Python', categoria='Programação', nivel='Básico')
presentation(curso1='PHP', categoria='Programação', nivel='Básico')