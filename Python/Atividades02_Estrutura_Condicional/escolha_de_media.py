'''
Em uma escola, um professor deve realizar três avaliações por semestre.
Para o cálculo da nota final, ele pode usar três diferentes métodos de
cálculo de médias:

Média aritmética ("a");
Média ponderada ("p"): nesse caso, o programa deve perguntar também os
pesos de cada nota;
Média harmônica ("h"): pode ser definida pela quantidade de notas 
dividida pela soma do inverso de cada nota e informa a situação dos
alunos. Ex.: Se as notas forem 10, 7 e 5, a média harmônica será 3/(1/10+1/7+1/5);

Faça um programa que calcula uma das três médias para um conjunto de 3
notas. O usuário deve também informar (por meio de um único caractere)
qual média ele gostaria de usar.
'''

tipo_media = input()
controle = True

if tipo_media != 'a' and tipo_media != 'p' and tipo_media != 'h':
    print('Escolha um tipo de media valida.')
    controle = False

elif tipo_media == 'a':
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())
    media = (n1 + n2 + n3)/3

elif tipo_media == 'p':
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())
    p1 = int(input())
    p2 = int(input())
    p3 = int(input())
    media = (n1 * p1 + n2 * p2 + n3 * p3)/(p1 + p2 + p3)

elif tipo_media == 'h':
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())
    media = 3/(1/n1 + 1/n2 + 1/n3)

if controle == True:
    if 70 <= media <= 100:
        print(f'{media:.2f}')
        print('Aprovado')
    elif 40 < media < 70:
        print(f'{media:.2f}')
        print('Final')
    elif 0 <= media <= 40:
        print(f'{media:.2f}')
        print('Reprovado')
    else:
        print(f'{media:.2f}')
        print('Média inválida')