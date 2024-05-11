import math

cateto_adj = (float(input('digite o cateto adjacente em seu valor n²: ')))
cateto_oposto = (float(input('digite o cateto oposto em seu valor m²: ')))

hipotenusa = math.hypot(cateto_adj, cateto_oposto)

print(hipotenusa)