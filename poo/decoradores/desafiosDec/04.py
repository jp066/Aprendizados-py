def repetir_execucao(vezes):
    # repetir_execucao é chamada com o argumento 3
    def decorador(funcao):
        # decorador é chamada com a função mensagem como argumento
        def wrapper(*args, **kwargs):
            # wrapper é a função que será executada no lugar de mensagem
            for _ in range(vezes):  # _ é uma variável que não será usada
                resultado = funcao(*args, **kwargs) # resultado é a execução da função mensagem
            return resultado
        return wrapper
    return decorador

@repetir_execucao(3)
def mensagem():
    print('executando...')

# Quando mensagem() é chamado, wrapper() é executado
mensagem()