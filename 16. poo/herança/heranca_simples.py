class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Motocicleta(Veiculo):
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    
    def __init__(self, cor, placa, numero_rodas, carregado): # sobrescrevendo o método __init__ da classe Veiculo. como se fosse o @Override do flutter
        super().__init__(cor, placa, numero_rodas) # chamando o método __init__ da classe Veiculo como se fosse o super() do flutter
        self.carregado = carregado # adicionando um novo atributo à classe Caminhao como se fosse o this do flutter

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado") # a estrutura se chama ternário, é uma forma de fazer um if else em uma linha só
        # sintaxe: 
        # - valor_se_verdadeiro if condição else valor_se_falso


moto = Motocicleta("preta", "abc-1234", 2)
carro = Carro("branco", "xde-0098", 4)
caminhao = Caminhao("roxo", "gfd-8712", 8, True)

print(moto)
print(carro)
print(caminhao)