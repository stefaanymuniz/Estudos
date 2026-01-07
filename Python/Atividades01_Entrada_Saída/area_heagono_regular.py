'''
Escreva um programa em Python3 que peça o valor do lado de um hexágono regular, calcule e imprima sua área e seu perímetro.
Sabemos que um hexágono regular é o polígono de 6 lados iguais e com todos os ângulos internos iguais entre si.
Sabemos ainda que um hexágono regular de lado L é formado por 6 triângulos equiláteros de lado L.
'''

lado_hex = int(input())
area = ((lado_hex**2 * 3**0.5)/4) * 6
perimetro = lado_hex * 6

print('Lado do hexagono:', "%.1f" % lado_hex, 'metros,')
print('Area:', area, 'metros quadrados,')
print('Perimetro:',  "%.1f" %  perimetro, 'metros.')