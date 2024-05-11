n1 = int(input('digite sua nota: '))
n2 = int(input('digite sua nota: '))
n3 = int(input('digite sua nota: ')) 
n4 = int(input('digite sua nota: '))

total = (n1+n2+n3+n4) / 4

if(total >= 7):
    print('voce esta aprovado')
else:
    print('voce está reprovado')