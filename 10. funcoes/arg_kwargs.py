# aprender args e kwargs

def teste(nome, *args, **kwargs):
    print(nome)
    print(args)
    print(kwargs)
    
    
teste = teste("Lucas", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, idade=20, cidade="São Paulo") # args e kwargs são opcionais


def teste2(nome, *tupla, **dicionario):
    print(nome)
    print(tupla)
    print(dicionario)
    
    
teste2 = teste2("Lucas", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, idade=20, cidade="São Paulo") # args e kwargs são opcionais

print(f"{teste}\n")
print(f"{teste}\n") 

# O *args é uma lista de argumentos posicionais, enquanto o **kwargs é um dicionário de argumentos nomeados. resumindo, args é uma tupla e kwargs é um dicionário.