# função lambda é uma função anônima, ou seja, não possui um nome, e é usada para operações simples e rápidas. ex:
# lambda sempre recebe um argumento e retorna um valor.
# a sintaxe é: lambda argumento: operação
#power = lambda x: x**2 # lambda é a palavra-chave, x é o argumento, e x**2 é a operação que será realizada.
#print(power(5)) # 5**2 = 25

movie_l = ['titanic', 'avatar', 'star wars', 'harry potter', 'the lord of the rings']
ratings = {
    'titanic': [5,3],
    'avatar': [4,4],
    'star wars': [5,4],
    'harry potter': [4.5,5],
    'the lord of the rings': [5,5]
}

calc_media = lambda movie_name: sum(ratings[movie_name]) / len(ratings[movie_name])
    
recommend = lambda movie_name: f'recomendo assistir o filme {movie_name} pela media de {calc_media(movie_name)}'
for movie in movie_l:
    if calc_media(movie) > 4.5:
        print(recommend(movie))
    

for movie in movie_l:
    print(f'{movie} - {calc_media(movie)}')
