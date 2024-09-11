def mensagem(nome):
    print('exexutando mensagem')
    return f'oi {nome}'


def mensagem2(nome):
    print('exexutando mensagem2')
    return f'oi {nome}'


def executa(funcao, nome):
    print('executando executa')
    return funcao(nome)


executa(mensagem, 'Maria')
executa(mensagem2, 'João')