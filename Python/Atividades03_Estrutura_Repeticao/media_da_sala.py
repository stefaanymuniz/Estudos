'''
Um professor precisa saber qual a média das notas de uma sala e pediu
sua ajuda para construir um programa que permita inserir as notas finais
de cada aluno e, ao final, exibir a média da sala. Lembre-se que as notas
variam de 0 a 10 e o professor digitará -1 quando quiser encerrar as entradas
'''

soma_notas = 0
quant_notas = 0

while True:
    notas_finais = float(input())
    if notas_finais == -1:
        break
    soma_notas += notas_finais
    quant_notas += 1

media = soma_notas/quant_notas
print(f'{media:.2f}')