def somar(a, b):
    return a + b

def exibir(a,b,funcao):
    resultado = funcao(a,b)
    print(f'a soma de {a} + {b} é {resultado}')
    
    
exibir(10,20,somar) # a soma de 10 + 20 é 30


# **Objetos de primeira classe**:
# - Em Python, funções são objetos de primeira classe, o que significa que elas podem ser passadas como argumentos, 
#   retornadas por outras funções e atribuídas a variáveis.
# - Isso permite que você use funções como qualquer outro tipo de dado.
# - Isso é útil para passar funções como argumentos para outras funções, como no exemplo acima.
#   no exemplo acima, a função `exibir` recebe três argumentos: `a`, `b` e `funcao`.
#   A função `exibir` chama a função `funcao` passando os argumentos `a` e `b` e exibe o resultado.
# - Neste caso, a função `somar` é passada como argumento para a função `exibir`. 
#   é como se o parametro funcao fosse apenas um modo de chamar a função somar, ou seja, a função somar é chamada dentro da função exibir.