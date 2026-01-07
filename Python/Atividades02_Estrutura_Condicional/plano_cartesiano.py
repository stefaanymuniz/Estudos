'''
Faça um programa que leia da entrada padrão duas coordenadas
(x e y em sequência) referente a um ponto qualquer e imprime
em qual quadrante do plano cartesiano o referido ponto se encontra.

Os pontos que se encontram sobre um dos eixos (quando x ou y
for zero) não se encontram em quadrante algum. Nesse caso,
você deve imprimir sobre qual eixo o ponto está, ou se o 
ponto encontra-se sobre a origem
'''

x = int(input())
y = int(input())

if x == 0 and y == 0:
    print('Sobre a origem')
elif x == 0:
    print('Sobre o eixo y')
elif y == 0:
    print('Sobre o eixo x')
elif x >= 1 and y >= 1:
    print('Primeiro Quadrante')
elif x <= -1 and y >= 1:
    print('Segundo Quadrante')
elif x <= -1 and y <= -1:
    print('Terceiro Quadrante')
elif x >= 1 and y <= -1:
    print('Quarto Quadrante')