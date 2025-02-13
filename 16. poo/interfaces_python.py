from abc import ABC, abstractmethod, abstractproperty


class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property # propriedade siginiica que é um método que se comporta como um atributo
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
        print("Ligada!")

    def desligar(self):
        print("Desligando a TV...")
        print("Desligada!")

    @property
    def marca(self):
        return "Philco"


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ligado!")

    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Desligado!")

    @property
    def marca(self):
        return "LG"


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)


controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)

# em python, a interface é representada por uma classe abstrata que contém métodos abstratos.
# a classe que implementa a interface deve implementar todos os métodos abstratos da interface.
# a interface é uma forma de garantir que uma classe tenha um comportamento específico.
# por exemplo, a interface ControleRemoto define os métodos ligar, desligar e a propriedade marca.
# a classe ControleTV implementa a interface ControleRemoto e define os métodos ligar, desligar e a propriedade marca.
# a classe ControleArCondicionado implementa a interface ControleRemoto e define os métodos ligar, desligar e a propriedade marca.
# a interface ControleRemoto garante que todas as classes que a implementam tenham os métodos ligar, desligar e a propriedade marca.
# ela é como se fosse uma base para as classes que a implementam. como se servisse apenas para levar as outras classes os seus serviços.
# como um serviço de entrega de comida, por exemplo. ele não faz a comida, apenas leva a comida de um lugar para o outro.