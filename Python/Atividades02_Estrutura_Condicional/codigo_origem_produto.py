'''
Faça um programa que receba o código da origem de um produto e informe
em qual região ele foi produzido, ou seja, qual é a sua procedência.
Para isso utilize a tabela abaixo que associa o código de origem à região de procedência.

Código da Origem   Região de Procedência
1                   Nordeste
2                   Norte
3 e 4               Centro-Oeste
5 a 9               Sul
10 a 15             Sudeste
'''

codigo_origem = int(input())

if codigo_origem == 1:
    print('Nordeste')
    
elif codigo_origem == 2:
    print('Norte')
    
elif 3 <= codigo_origem <= 4:
    print('Centro-Oeste')
    
elif 5 <= codigo_origem <= 9 :
    print('Sul')
    
elif 10 <= codigo_origem <= 15 :
    print('Sudeste')