'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F. 
Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''

sexo = str(input('digite o seu sexo: ')).upper().strip()
while sexo not in 'MF':
    sexo = str(input('digite o seu sexo: ')).upper().strip()
print(f'Sexo {sexo} registrado com sucesso!')
