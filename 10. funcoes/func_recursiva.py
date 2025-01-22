# função recursiva é uma função que chama a si mesma, ou seja, ela é uma função que se chama dentro dela mesma.
# exemplo de função recursiva:

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1) # chama a função dentro dela mesma
    
    
number = int(input('Digite um número: '))
print(f'O fatorial de {number} é {factorial(number)}')

# é mais usada no desenvolvimento de algoritmos, por exemplo, para calcular fatorial, fibonacci, etc. 