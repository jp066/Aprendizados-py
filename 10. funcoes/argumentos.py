# argumentos em funcoes
# os argumentos sao passados para a funcao atraves dos parenteses, eles são as informações que a funcao precisa para executar a tarefa.
# ou seja, os argumentos são os valores que a função espera receber para realizar a tarefa.

def rate_movie(nume_rate, movie):
    total = 0
    for i in range(nume_rate):
        rate = int(input(f'Qual a sua nota para o filme {movie}? '))
        total += rate        
    if nume_rate > 0:
        average = total / nume_rate
    else:
        average = 0
    print (f'A média das notas para o filme {movie} é {average:.1f}')


rate_movie(2, 'Matrix')