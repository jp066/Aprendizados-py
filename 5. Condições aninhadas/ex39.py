from datetime import date

atual = date.today().year
nascimento = int(input("qual seu ano de nascimento? "))
idade = atual - nascimento
restante = nascimento - 2006

if (idade == 18):
    print("Você está no ano de alistamento!")
elif (idade > 18):
    print("Você já passou do tempo de alistamento!")
else:
    print(f"Você ainda precisa de {restante} anos para se alistar!")