import time

def medir_tempo(funcao):
    def temp_execucao(*args, **kwargs):
        inicio = time.time()
        resultado = funcao(*args, **kwargs)
        fim = time.time()
        print(f'Tempo de execução: {fim - inicio}')
        return resultado
    return temp_execucao

@medir_tempo
def tarefa_demorada(i):
    for i in range(100000):
        pass    
    
print(tarefa_demorada(1)) # tarefa_demorada = medir_tempo(tarefa_demorada)()