nota1 = float(input("digite a nota 1: "))
nota2 = float(input("digite a nota 2: "))

media = (nota1 + nota2)/2

if (media >= 7):
    print(f"sua media é {media}, voce está aprovado!!")

elif (media >= 5 and media < 7):
    print(f"sua media é {media}, voce está de recuperação!!")

elif (media <= 5):
    print(f"sua media é {media}, voce está reprovado!!")