# **Parâmetros por posição**:
def por_posicao(nome, idade):
    print(nome)
    print(idade)
    return nome, idade
por_posicao("Lucas", 20) # parâmetros por posição


# **Parâmetros por nome**:
def por_nome(nome="Lucas", idade=20):
    print(nome)
    print(idade)
    return nome, idade
por_nome(idade=20, nome="Lucas") # parâmetros por nome


# **Parâmetros por posição e nome**:
def por_posicao_nome(nome, idade=20):
    print(nome)
    print(idade)
    return nome, idade
por_posicao_nome("Lucas", 20) # parâmetros por posição e nome


# **Uso de `/` e `*` para definir se os argumentos são passados por posição ou por nome**:
# - / - define que os argumentos anteriores a ele são passados por posição.
# - * - define que os argumentos após ele são passados por nome.
# Exemplos:


def exemplo1(nome, /, idade):
    print(nome)
    print(idade)
    return nome, idade

exemplo1("Lucas", idade=20) # parâmetros por posição e nome

def exemplo2(nome, *, idade):
    print(nome)
    print(idade)
    return nome, idade

exemplo2("Lucas", idade=20) # parâmetros por posição e nome
