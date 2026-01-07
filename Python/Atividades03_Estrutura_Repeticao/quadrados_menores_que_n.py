'''Todos os quadrados menores que n.'''

quadrado_maior = int(input())
n = 0

while n**2 < quadrado_maior:
    print(n**2)
    n += 1