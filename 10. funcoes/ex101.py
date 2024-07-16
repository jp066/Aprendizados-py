# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
from datetime import date

def voto(ano):
    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade >= 18:
        return 'Voto OBRIGATÓRIO'
    
    elif idade >= 16:
        return 'Voto OPCIONAL'
    
    else:
        return 'Voto NEGADO'
    
    
print(voto(2006))