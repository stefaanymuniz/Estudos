'''
Faça um programa que leia três coordenadas num
espaço 2D e indique se formam um triângulo,
juntamente com o seu tipo (equilátero, isósceles e
escaleno)

◼ Equilátero: todos os lados iguais
◼ Isósceles: dois lados iguais
◼ Escaleno: todos os lados diferentes
'''

coord1 = float(input('Digite o primeiro comprimento do triângulo: '))
coord2 = float(input('Digite o segundo comprimento: '))
coord3 = float(input('Digite o terceiro comprimento: '))

if coord1 + coord2 > coord3 and coord1 + coord3 > coord2 and coord2 + coord3 > coord1:
    if coord1 == coord2 == coord3:
        print('O triângulo é do tipo Equilátero')
    
    #elif coord1 == coord2 != coord3 or coord1 != coord2 == coord3 or coord2 == coord1 != coord3 or coord2 != coord1 == coord3: (errado)
    elif coord1 == coord2 or coord2 == coord3 or coord1 == coord3:
        print('O triângulo é do tipo Isósceles')
        
    elif coord1 != coord2 != coord3:
        print('O triângulo é do tipo Escaleno')
else:
    print('Os comprimentos não formam um triângulo válido')