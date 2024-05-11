# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher 
# qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

#binary_number = bin(decimal_number)
#octal_number = oct(decimal_number)
#hexadecimal_number = hex(decimal_number)

num_inteiro = int(input('digite um numero inteiro qualquer: '))
opcao = int(input('''escolha entre:
1(binário)
2(octal)
3(hexadecimal): '''))

if (opcao == 1):
    num_binario = bin(num_inteiro)
    print(num_binario[2:])
elif (opcao == 2):
    num_octal = oct(num_inteiro)
    print(num_octal[2:])
elif (opcao == 3):
    num_hexadecimal = hex(num_inteiro)
    print(num_hexadecimal[2:])