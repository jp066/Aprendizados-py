def contador_chamadas(funcao):
    def contar(*args, **kwargs):
        contar.chamadas *= 1
        print(f'Esta função foi chamada {contar.chamadas} vezes')
        contar.chamadas += 1
        return funcao(*args, **kwargs) # nessa linha a função soma é chamada pela referência funcao, como se fosse soma(10,10)
    contar.chamadas = 1
    return contar

@contador_chamadas
def soma(x,y):
    return x + y


print(soma(10,10))
print(soma(10,10))
print(soma(10,10))