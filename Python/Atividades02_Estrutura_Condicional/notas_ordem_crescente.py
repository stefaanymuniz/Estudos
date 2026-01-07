'''
Escreva um programa que leia as notas de três pessoas pessoas
em uma prova e as exiba na saída padrão de forma crescente (0 á 100).
'''

n1 = int(input())
n2 = int(input())
n3 = int(input())

if (n1 >= n2 >= n3): 
    print(n3)
    print(n2)
    print(n1)

elif (n1 >= n3 >= n2):
    print(n2)
    print(n3)
    print(n1)

elif (n2 >= n1 >= n3):
    print(n3)
    print(n1)
    print(n2)

elif (n2 >= n3 >= n1):
    print(n1)
    print(n3)
    print(n2)

elif (n3 >= n1 >= n2 ):
    print(n2)
    print(n1)
    print(n3)

elif (n3 >= n2 >= n1):
    print(n1)
    print(n2)
    print(n3)
else:
    print('Digite três números válidos de 0 á 100.')