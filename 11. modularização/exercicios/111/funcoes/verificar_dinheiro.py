def ler_dinheiro(valor):
    while True:
        valor = input('Digite o preço: R$')
        if valor.isalpha() or valor == '':
            print(f'\033[31mERRO: "{valor}" é um preço inválido!\033[m')
        else:
            return float(valor)