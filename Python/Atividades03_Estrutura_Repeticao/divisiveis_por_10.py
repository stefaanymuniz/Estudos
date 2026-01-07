'''Todos os números positivos que são divisíveis por 10 e menores que n'''

n = int(input())
contagem = 1

while contagem < n:
    if contagem % 10 == 0:
        print(contagem)
    contagem += 1 