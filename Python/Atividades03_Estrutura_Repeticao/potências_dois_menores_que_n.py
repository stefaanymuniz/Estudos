'''Todas as potências de dois menores que n'''

n = int(input())
contagem = 0

while 2**contagem < n:
    print(2**contagem)
    contagem += 1