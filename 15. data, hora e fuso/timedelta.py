# objetos timedelta representa uma diferença entre duas datas ou horas
from datetime import datetime, timedelta

data_atual = datetime.now()
tipo_carro = 'M'
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60

if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f'o carro pequeno será entregue em {data_estimada}')

elif tipo_carro == 'M':
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f'o carro médio será entregue em {data_estimada}')

elif tipo_carro == 'G':
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f'o carro grande será entregue em {data_estimada}')