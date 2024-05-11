distancia = int(input('qual a distancia de sua viagem? '))

if distancia <= 200:
    preco_passagem = distancia * 0.50
    print(f"o preco da sua viagem é de {preco_passagem}")
else:
    preco_passagem = distancia * 0.45
    print(f"o preco da sua viagem é de {preco_passagem}")