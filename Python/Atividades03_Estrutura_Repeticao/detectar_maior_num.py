maior_num = 0

while True:
    n = int(input())

    if n == 0:
        break
    elif n > maior_num:
        maior_num = n

print(maior_num)