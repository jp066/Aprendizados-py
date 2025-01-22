# list comprehession é uma forma de criar listas de forma mais rápida e limpa, usando uma única linha de código
# sem a necessidade de usar loops, é basicamente uma forma de criar listas de forma mais rápida e limpa
# por que usar list comprehession? por que é mais rápido e limpo que usar loops

# sintaxe: [expression for item in list if condition]


moviesList = ['star wars', 'star trek', 'gattaca', 'alien', 'terminator', 'inception', 'matrix']

moviesWithE = [movie for movie in moviesList if movie.find('e') > -1]
print(moviesWithE)  # ['star trek', 'terminator', 'inception', 'matrix']


moviesWatched = [movie for movie in moviesList if movie != 'star wars']
print(moviesWatched)  # ['star trek', 'gattaca', 'alien', 'terminator', 'inception', 'matrix']

while True:
    searchName = input('Digite o nome de um filme: (Q para sair) ')
    if searchName.upper() == 'Q':
        break
    foundMovies = [movie for movie in moviesList if searchName.lower() in movie.lower()] # se o filme for encontrado, ele será adicionado a lista
    if foundMovies:
        print(f'Filme encontrado: {foundMovies}')
    else:
        print('Filme não encontrado')