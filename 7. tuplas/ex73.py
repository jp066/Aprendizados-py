# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. 
# Depois mostre:
# 
# a) Os 5 primeiros times.
# 
# b) Os últimos 4 colocados.
# 
# c) Times em ordem alfabética.
# 
# d) Em que posição está o time da Chapecoense.

times = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras', 'Santos', 'Athletico-PR', 'Bragantino', 'Ceará', 'Corinthians', 'Atlético-GO', 'Bahia', 'Sport', 'Fortaleza', 'Vasco', 'Goiás', 'Coritiba', 'Botafogo')

print(f'Os 5 primeiros times são: {times[:5]}')
print(f'Os 4 últimos colocados são: {times[-4:]}')
print(f'Times em ordem alfabética: {sorted(times)}')

if 'Chapecoense' in times:
    print(f'O time da Chapecoense está na {times.index("Chapecoense")+1}ª posição')
else:
    print('Chapecoense não está na lista de times')