# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, 
# só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt():
    ok = False
    valor = 0
    while True:
        numero = str(input('Digite um número: '))
        if numero.isnumeric():
            valor = int(numero)
            ok = True
            return valor
        else:
            print('ERRO! Digite um número inteiro válido.')
        if ok:
            break
        
print(leiaInt())