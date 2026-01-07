valores = list()
contador = 0

for _ in range(10):
    valores.append(int(input()))

num_procurado = int(input())

for valor in valores:
    if num_procurado == valor:
        contador += 1

print(contador)
