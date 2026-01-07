def congruente(i, j, m):
    if i < 1 or j < 1 or m < 1:
        print(-1)
    for _ in range(i):
        print(j)
        j += m


i = int(input()) # quantidade de vezes
j = int(input()) # número que inicia
m = int(input()) # somar ao número que inicia

congruente(i, j, m)