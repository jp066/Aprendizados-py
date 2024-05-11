soma = 0
cont = 0

for c in range(1, 7):
    num = int(int(input(f'digite {c}:')))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'a soma deu {soma}')