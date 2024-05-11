n = s = 0
while True:
    num = int(input('digite um numero: '))
    if num == 999:
        break
    s += num
print(f'a soma dos valores {s}')