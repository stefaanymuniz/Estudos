def calcula_indice(desempenho, gols, cansaco, entrosamento):
    # 2 características no nível mínimo seu índice será zero:
    caracteristicas_baixas = 0
    if desempenho == 0:
        caracteristicas_baixas += 1
    if gols == 0 :
        caracteristicas_baixas += 1
    if cansaco == 0: 
        caracteristicas_baixas += 1
    if entrosamento == 0:
        caracteristicas_baixas += 1
        
    if caracteristicas_baixas >= 2:
        return 0
    else:
        indice = desempenho * 2 + gols * 3.5 + cansaco * 1.5 + entrosamento * 2
        return indice

indices = []

for _ in range(5):
    nome_jogador = input()
    desempenho = int(input()) # 0 = "ruim, 1 = "mediano", 2 = "bom"
    gols_feitos = int(input())
    nivel_cansaco = int(input()) # 0 = "muito cansado", 1 = "pouco cansado", 2 = "descansado"
    entrosamento = int(input()) # 0 = "baixo", 1 = "médio", 2 = "alto"

    # Calcula o índice técnico e adiciona diretamente à lista
    indices.append(calcula_indice(desempenho, gols_feitos, nivel_cansaco, entrosamento))

indices_ordenados = sorted(indices, reverse = True)
maior_indice01 = indices_ordenados[0]
maior_indice02 = indices_ordenados[1]
maior_indice03 = indices_ordenados[2]

print(maior_indice01)
print(maior_indice02)
print(maior_indice03)