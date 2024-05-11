from random import randint
print('-=-' * 20)
escolha = int(input('digite sua escolha de 0 a 5: '))
print('-=-' * 20)

numero_gerado = randint(0, 5)

if numero_gerado == escolha:
    print('-=-' * 20)
    print(f"voce acertou!!, o numero é {escolha}")
    print('-=-' * 20)
else: 
    print('-=-' * 20)
    print(f"voce errou, o numero era {numero_gerado}")
    print('-=-' * 20)