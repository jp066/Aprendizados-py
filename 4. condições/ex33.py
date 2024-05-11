numero1 = int(input('1. digite um numero: '))
numero2 = int(input('2. digite um numero: '))
numero3 = int(input('3. digite um numero: '))

if numero1 < numero2 and numero1 < numero3:
    print('o numero 1 é menor.')
elif numero2 < numero1 and numero2 < numero3:
    print('o numero 2 é menor.')
elif numero3 < numero1 and numero3 < numero2:
    print('o numero 3 é menor.')