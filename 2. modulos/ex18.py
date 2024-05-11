import cmath
import math

angulo = float(input('Digite o ângulo em graus: '))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f"Cosseno: {cosseno :.2f}")
print(f"Seno: {seno :.2f}")
print(f"Tangente: {tangente :.2f}")