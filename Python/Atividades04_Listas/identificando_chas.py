votos_corretos = 0
tipo_cha = int(input())

if tipo_cha < 0 or tipo_cha > 4:
    print('Selecione um número válido.')

# Para coletar os valores em string e convertê-los em int numa mesma linha:
votos_participantes = [int(valor) for valor in input().split()]

for voto in votos_participantes:
    if voto == tipo_cha:
        votos_corretos += 1

print(votos_corretos)
