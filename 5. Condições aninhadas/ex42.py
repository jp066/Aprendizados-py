# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# 
# – EQUILÁTERO: todos os lados iguais
# 
# – ISÓSCELES: dois lados iguais, um diferente
# 
# – ESCALENO: todos os lados diferentes

a = int(input('1. digite o valor da reta: '))
b = int(input('2. digite o valor da reta: '))
c = int(input('3. digite o valor da reta: '))

if (a == b == c):
    print(f"pode formar um triangulo EQUILÁTERO de lados {a, b, c}")
elif (a != b != c):
    print(f"pode formar um triangulo ESCALENO de lados {a, b, c}")
else:
    print(f"pode formar um triangulo ISÓSCELES de lados {a, b, c}")