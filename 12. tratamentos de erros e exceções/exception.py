# while True:
#     try:
#         velocidade = int(input('Digite a velocidade: '))
#         if velocidade > 100:
#            pode_passar = False
#            raise ValueError('Velocidade perigosa!')
#     else:
#            # Se a velocidade for 100 ou menos, é considerada segura
#            pode_passar = True
#     except ValueError as error:
#       print(f'Alerta de segurança: {error}')
#     if pode_passar:
#       print('Velocidade segura!')
#       break

# try:
#     num = int(input('Digite um número: '))
#     num2 = int(input('Digite outro número: '))
#     resultado = num / num2
# except Exception as error:
#     print(f'Erro: {error.__class__}')
# else:
#     print(f'O resultado da divisão é: {resultado}')
# finally:
#     print('Fim do programa')