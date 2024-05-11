salario = float(input('digite seu salario: '))

if salario > 1250:
    aumento = salario * 0.10
    salario += aumento
    print(salario)
else:
    aumento = salario * 0.15
    salario += aumento
    print(salario)