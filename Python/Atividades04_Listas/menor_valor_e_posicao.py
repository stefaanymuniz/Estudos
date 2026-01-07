valores = []
quant_valores = int(input())
valores_str = input().split() # O ".split()" não aceita valores int, então tem que converte-los

# Pega cada valor na lista de strings para transformá-los em valores inteiros
for valor in valores_str:
    valores.append(int(valor))

menor_num = min(valores)
posicao_menor_num = valores.index(menor_num)

print(f'Menor valor: {menor_num}')
print(f'Posicao: {posicao_menor_num}')