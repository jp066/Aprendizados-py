# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

km = int(input('qual a velocidade do carro? '))
multa = float((km - 80) * 7)

if(km > 80):
    print(f"voce foi multado no valor de R$ {multa}")
else:
    print('sem multas para você!!')