from math import trunc

# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) 
# e mostre seu status, de acordo com a tabela abaixo:
# 
# – IMC abaixo de 18,5: Abaixo do Peso
# 
# – Entre 18,5 e 25: Peso Ideal
# 
# – 25 até 30: Sobrepeso
# 
# – 30 até 40: Obesidade
# 
# – Acima de 40: Obesidade Mórbida

peso = float(input('qual seu peso? '))
altura = float(input('qual sua altura? '))

imc = peso / (altura * altura)

if (imc < 18.5):
    print(f"seu imc é {trunc(imc)} e vocé está abaixo do peso normal")

if (imc >= 18.5 and imc < 25):
    print(f"seu imc é {trunc(imc)} e vocé está no peso ideal")

if (imc >= 125 and imc < 40):
    print(f"seu imc é {trunc(imc)} e vocé está com obesidade")

if (imc > 40):
    print(f"seu imc é {trunc(imc)} e vocé está com obesidade mórbida")