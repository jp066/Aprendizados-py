a = int(input('1. digite o valor da reta: '))
b = int(input('2. digite o valor da reta: '))
c = int(input('3. digite o valor da reta: '))

if (a+b > c and a+c > b and b+c >a):
    print(f"pode formar um triangulo de lados {a, b, c}")
else:
    print('não se pode formar um triangulo.')