# Exercício "Q3 - Quantos números são maiores ou menores que uma variação da média?" do The Huxley

soma_notas = 0
notas = []
quant_notas = int(input())

for i in range(quant_notas):
    nota = float(input())
    notas.append(nota)
    soma_notas += nota

media = soma_notas/quant_notas
acima_media = []
abaixo_media = []

for nota in notas:
    if nota > media+media*0.1:
        acima_media.append(nota)
    elif nota < media-media*0.1:
        abaixo_media.append(nota)
    
print(f'{media:.2f}')
print(len(acima_media))
print(len(abaixo_media))