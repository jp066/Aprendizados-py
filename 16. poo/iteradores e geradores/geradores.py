# tipos especiais de iteradores, não armazenam todos os valores na memória, apenas um de cada vez.
# definidos usando funções regulares que contêm palavras-chave yield. ao inves de return.
# uma vez consumido o valor, ele é descartado da memória.
# o estado da função é mantido entre as chamadas.
# a execução é pausada e retomada quando a função é chamada novamente.

def meu_gerador(numeros: list[int]):
    for numero in numeros: 
        yield numero * 2
    
    
for i in meu_gerador(numeros=[10, 20, 30, 40, 50]):
    print(i)