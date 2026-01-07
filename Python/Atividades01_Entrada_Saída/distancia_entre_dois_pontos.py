'''
Escreva um programa que calcula a distância d entre dois pontos
A e B no espaço, isto é, com coordenadas (x, y, z)
'''

pontoA_x = float(input())
pontoA_y = float(input())
pontoA_z = float(input())
pontoB_x = float(input())
pontoB_y = float(input())
pontoB_z = float(input())

distancia_AB = (((pontoB_x - pontoA_x)**2) + ((pontoB_y - pontoA_y)**2) + ((pontoB_z - pontoA_z)**2))**0.5
print(distancia_AB)
