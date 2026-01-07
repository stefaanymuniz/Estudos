'''
Escreva um programa que recebe 3 notas de prova e calcula:

- A média delas
- A média ponderada delas, considerando pesos 2, 2 e 3
- A média ponderada delas, considerando pesos 1, 2 e 2

'''

n1 = float(input())
n2 = float(input())
n3 = float(input())

media1 = (n1 + n2 + n3)/3
media2 = ((n1 * 2) + (n2 * 2) + (n3 * 3)) / 7
media3 = ((n1 * 1) + (n2 * 2) + (n3 * 2)) / 5
print(media1)
print(media2)
print(media3)