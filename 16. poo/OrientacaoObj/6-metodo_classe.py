class Game:
    total_games = 0 # Variável de classe para contar o número total de jogos
    def __init__(self, name="", yearLaunch=0, multiplayer=0, note=0):
        self.name = name  
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note
        Game.total_games += 1
        self.totalEvaluation = 0
        self.evaluators = 0
        
    def __str__(self):
        return f"Game: {self.name}"
    
    def technical_sheet(self):
        print("###Dados do Jogo###")
        print(f"Nome do jogo: {self.name}")
        print(f"Ano de Lançamento: {self.yearLaunch}")
        print(f"Modo multiplayer?: {self.multiplayer}")
        print(f"Avaliação do Jogo: {self.note}\n")
        
    def evaluate(self, note):
        self.totalEvaluation += note
        self.evaluators += 1
        
    def average(self):
        print(f"Média do jogo {self.name}: {self.totalEvaluation / self.evaluators}")
        
    @classmethod
    def print_total_games_stats(cls):
        print("####Estatísticas Gerais dos Jogos####")
        print(f"Total de jogos criados: {cls.total_games}")
        cls.average(cls)
        
game1 = Game("The Legend of Zelda", 2017, False, 9.5)
game2 = Game("Fortnite", 2017, True, 8.0)
game3 = Game("Red Dead Redemption 2", 2018, False, 10.0)

game1.technical_sheet()
game2.technical_sheet()
game1.evaluate(9.0)
game1.evaluate(7.5)
game2.evaluate(6.5)
game2.evaluate(7.5)

Game.print_total_games_stats()


# method class é um método que é acessado pela classe, e não pelo objeto.
# Ele é utilizado quando se deseja criar um método que seja comum a todos os objetos da classe.
# analogia da vida real: seria como um método que é comum a todos os funcionários de uma empresa, tipo calcular o salário.
# ex:
# class Funcionario:
#     def __init__(self, nome, salario):
#         self.nome = nome
#         self.salario = salario
#
#     def calcular_salario(self):
#         return self.salario
#
#     @classmethod
#     def calcular_salario_com_imposto(cls, salario):
#         return salario - (salario * cls.imposto)
#
#     @staticmethod
#     def calcular_salario_com_imposto(salario, imposto):
#         return salario - (salario * imposto)
#
# funcionario1 = Funcionario("João", 1000)
# print(funcionario1.calcular_salario())
# print(Funcionario.calcular_salario_com_imposto(1000))
# print(Funcionario.calcular_salario_com_imposto(1000, 0.1))
# print(funcionario1.calcular_salario_com_imposto(1000))
# print(funcionario1.calcular_salario_com_imposto(1000, 0.1))