class Game:
    name = ""
    yearLaunch = 0
    multiplayer = False
    note = 0

# Primeiro jogo
game1 = Game()
game1.name = "The Legend of Zelda: Breath of the Wild"
game1.yearLaunch = 2017
game1.multiplayer = False
game1.note = 9.5

# Segundo jogo
game2 = Game() # Instanciando um novo objeto da classe Game
game2.name = "Fortnite"
game2.yearLaunch = 2017
game2.multiplayer = True
game2.note = 8.0

# Terceiro Jogo
game3 = Game()
game3.name = "Jedi Star Wars: Fallen Order"
game3.yearLaunch = 2019
game3.multiplayer = False
game3.note = 9.0

# Quarto Jogo
game4 = Game()
game4.name = "EA FC 25"
game4.yearLaunch = 2024
game4.multiplayer = True
game4.note = 6.9

print("###Dados do Jogo###")
print(f"\nNome do jogo: {game1.name}\nAno de Lançamento: {game1.yearLaunch}")
print(f"\nNome do jogo: {game2.name}\nAno de Lançamento: {game2.yearLaunch}")

# na poo, a classe representa algo que tenha outros usuarios, que podem personalizar suas propriedades.
# e os meotodos são as ações que esses objetos podem fazer.