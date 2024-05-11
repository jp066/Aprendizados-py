# Faça um programa que leia o peso de cinco pessoas. 
# No final, mostre qual foi o maior e o menor peso lidos.
pesoMaior = 0
pesoMenor = 0
for p in range (1,6):
    peso = int(input(f'qual o peso da {p}° pessoa: '))
    if p == 1:
        pesoMaior = peso
        pesoMenor = peso
    else:
        if peso > pesoMaior:
            pesoMaior = peso
        if peso < pesoMenor:
            pesoMenor = peso
print(f'o maior peso foi {pesoMaior}')
print(f'o menor peso foi {pesoMenor}')