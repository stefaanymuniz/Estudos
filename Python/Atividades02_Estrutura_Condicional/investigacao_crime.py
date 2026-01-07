'''Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:"Telefonou para a vítima?""Esteve no local do crime?"
"Mora perto da vítima?""Devia para a vítima?""Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da
pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve
ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como
"Assassino". Caso contrário, ele será classificado como "Inocente".'''

telefonou = input('Telefonou para a vítima? ')
local_crime = input('Esteve no local do crime? ')
mora_perto = input('Mora perto da vítima? ')
devedor = input('Devia para a vítima? ')
colega_trabalho = input('Já trabalhou com a vítima? ')

respostas = 0

if telefonou == 'Sim':
    respostas += 1
if local_crime == 'Sim':
    respostas += 1
if mora_perto == 'Sim':
    respostas += 1
if devedor == 'Sim':
    respostas += 1
if colega_trabalho == 'Sim':
    respostas += 1

if respostas == 5:
    print('Assassino')
elif 3 <= respostas <= 4:
    print('Cumplice')
elif respostas == 2:
    print('Suspeita')
elif respostas == 0:
    print('Inocente')

# Forma não tão inteligente de se fazer:
# if telefonou == 'Nao' and local_crime == 'Nao' and mora_perto == 'Nao' and devedor == 'Nao' and colega_trabalho == 'Nao':
#     print('Inocente')
# else:
#     if telefonou == 'Sim' and local_crime == 'Sim' and mora_perto == 'Sim' and devedor == 'Sim' and colega_trabalho == 'Sim':
#         print('Assassino')
#     elif (telefonou == 'Sim' and local_crime == 'Sim' and mora_perto == 'Sim') or