valores = []
contador_maior_num = 0
contador_menor_num = 0

quant_elementos = int(input())

for _ in range(quant_elementos):
    valores.append(int(input()))

maior_num = max(valores)
menor_num = min(valores)

for valor in valores:
    if valor == maior_num:
        contador_maior_num += 1
    elif valor == menor_num:
        contador_menor_num += 1

print(f'Maior: {maior_num} apareceu {contador_maior_num} vezes')
print(f'Menor: {menor_num} apareceu {contador_menor_num} vezes')
