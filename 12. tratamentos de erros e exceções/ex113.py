# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(valor=0):
    ok = False
    while True:
        numero = str(input('Digite um número: '))
        try:
            valor = int(numero)
            ok = True
            return f'valor: {valor}'
        
        except ValueError:
            print('ERRO! Digite um número inteiro válido.')
            
        except Exception as error:
            print(f'Erro: {error.__class__}')
            
        if ok:
            break
        
def leiaFloat(valor=0):
    ok = False
    while True:
        numero = str(input('Digite um número: '))
        try:
            valor = float(numero)
            ok = True
            return f'valor: {valor}'
        
        except ValueError:
            print('ERRO! Digite um número inteiro válido.')
            
        except Exception as error:
            print(f'Erro: {error.__class__}')
            
        if ok == True:
            break


print(f'''resumo:
      1 - {leiaInt()}
      2 - {leiaFloat()}''')