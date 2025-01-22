## 1
#def soma_num(*args):
#    return sum(args)
#print(soma_num(1, 2, 3, 4, 5))  # 15
#
#
## 2
#def mult_num(*kwargs):
#    numero_inicial = 1
#    for numero in kwargs:
#        numero_inicial = numero_inicial * numero
#    return numero_inicial
#print(mult_num(2, 3, 4))
#
#
## 3
#def mensagem(nome, *args):
#    print(f'Olá {nome}')
#    for msg in args:
#        print(f"- {msg}")
#    
#mensagem('João', 'tudo bem?', 'como vai?', 'você está bem?')
#
#
## 4
#def dic_info(nome, **kwargs):
#    print(f'Nome: {nome}')
#    for chave, valor in kwargs.items():
#        print(f'{chave}: {valor}')
#        
#dic_info('João', idade=30, cidade='São Paulo', profissao='programador')


# 5
#def filter_pares(*args):
#    return [numero for numero in args if numero % 2 == 0]
#print(filter_pares(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
#

# 6
def combinar_args_kwargs(*args, **kwargs):
    print(f"lista - {list(args)}")
    print(f"dict - {kwargs}")
    
combinar_args_kwargs(1, 2, 3, nome='João', idade=30, cidade='São Paulo')