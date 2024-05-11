from datetime import date

ano_nasc = int(input("digite seu ano de nascimento? "))
ano_atual = date.today().year
idade = ano_atual - ano_nasc

if (idade <= 9):
    print("o atleta é mirim")
elif (idade <= 14):
    print("o atleta é infantil")
elif (idade <= 19):
    print("o atleta é junior")
elif (idade <= 25):
    print("o atleta é senior")
else:
    print("o atleta é master")