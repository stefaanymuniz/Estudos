'''
A diagonal de um polígono é um segmento de linha que liga 2 vértices não adjacentes
Faça um programa que calcula a quantidade de diagonais de um polígono baseado na quantidade de lados desse polígono
'''

lados = int(input())
diagonais = (lados * (lados - 3))/2

print(round(diagonais))