def Multiplos(i, f, x):
    for sequencia in range(i, f + 1):
        if (sequencia % x == 0):
            print(sequencia)
            

i = int(input()) # Início do intervalo
f = int(input()) # Final do intervalo
x = int(input()) # Múltiplo

Multiplos(i, f, x)