soma = 0

while True:
    n = int(input())
    if n == 0:
        break
    elif n < 0:
        continue
    soma += n

print(f'A soma dos valores positivos eh: {soma}')