# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

expressao = str(input('digite uma expressao: ')).strip()
lista = []

for parenteses in expressao: # para cada parenteses na expressao
    if parenteses == '(': # e se o parenteses for igual a '('
        lista.append('(')
    elif parenteses == ')':
        if len(lista) > 0: # e se o tamanho da lista for maior que 0
            lista.pop() # remove o ultimo elemento da lista
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('sua expressao esta correta')
else:
    print('sua expressao esta errada')
    
print(lista)