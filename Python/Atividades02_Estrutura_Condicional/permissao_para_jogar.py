'''
Uma plataforma online oferece 4 tipos de jogos, onde Cada um desses tipos de jogo
tem uma faixa etária para que o jogador possa participar.

Jogos de azar - Apostas esportivas, blackjack, roleta e afins.
21 anos ou mais

MMORPG - Massively Multiplayer Online Role-Playing Game
14 anos ou mais

MOBA - Multiplayer Online Battle Arena
10 anos ou mais

Casual
Sem limite de idade

Faça um programa que receba a idade do jogador e o tipo de jogo que ele deseja
jogar e informe se ela pode jogar. Caso a idade do jogador caia fora do intervalo
válido ou seja informado um tipo de jogo que não existe, deve ser emitida uma
mensagem de erro de acordo com o que aconteceu.
'''

idade_jogador = int(input())
tipo_jogo = input()

if idade_jogador < 0 or idade_jogador > 130:
    print('Idade invalida.')

elif tipo_jogo != 'azar' and tipo_jogo != 'mmorpg' and tipo_jogo != 'moba' and tipo_jogo != 'casual':
    print('Jogo invalido')

elif tipo_jogo == 'azar' and idade_jogador >= 21:
    print('Pode entrar!')
    
elif tipo_jogo == 'mmorpg' and idade_jogador >= 14:
    print('Pode entrar!')

elif tipo_jogo == 'moba' and idade_jogador >= 10:
    print('Pode entrar!')

elif tipo_jogo == 'casual':
    print('Pode entrar!')

else:
    print('Volte daqui há alguns anos.') 
