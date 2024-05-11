# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
comprador = str(input('ola, como posso lhe chamar? '))
valor_casa = float(input('qual o valor da casa? '))
salario = float(input('qual o seu salario? '))
anos = int(input('em quantos anos pretende pagar? '))
prestacoes = valor_casa / (anos * 12)

if (prestacoes <= (0.3 * salario)):
    print('--------------------------------------------------------------------------------------------------------------------')
    print(f'compra aprovada no nome de {comprador}')
elif (prestacoes >= (0.3 * salario)):
    print('--------------------------------------------------------------------------------------------------------------------')
    print(f'compra negada no nome de {comprador} por falta de credito.')
print('--------------------------------------------------------------------------------------------------------------------')
print(f'sua prestação ficou de R${prestacoes} em {anos} anos ou {(anos*12)} meses')