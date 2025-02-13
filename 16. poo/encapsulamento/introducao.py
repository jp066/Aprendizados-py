class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.__titular = titular  # Atributo privado
        self.__saldo = saldo_inicial  # Atributo privado

    # Método público para depositar dinheiro
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    # Método público para sacar dinheiro
    def sacar(self, valor):
        if 0 < valor <= self.__saldo:
            self.__saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

    # Método público para consultar o saldo
    def consultar_saldo(self):
        return f"Saldo atual: R${self.__saldo:.2f}"

# # Exemplo de uso
conta = ContaBancaria("João Silva", 1000)
# print(conta.consultar_saldo())  # Saída: Saldo atual: R$1000.00
# conta.depositar(500)
# print(conta.consultar_saldo())  # Saída: Saldo atual: R$1500.00
# conta.sacar(200)
# print(conta.consultar_saldo())  # Saída: Saldo atual: R$1300.00

conta.__saldo = 5000  # Tentativa de modificar o atributo privado diretamente
print(conta.consultar_saldo())  # Ainda exibirá o saldo original, não o valor modificado
# em python nao existem obejtos privados. portanto, o atributo __saldo é acessível fora da classe, mas por convenção, não deve ser acessado diretamente.