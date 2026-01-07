# import random

# palpite = int(input('Olá jogador(a)! Tente adivinhar o número que estou pensando: '))
# numero_secreto = random.randint(1, 10)

# while palpite != numero_secreto:
#   palpite = int(input('Errou! Tente mais uma vez: '))

# print(f'Parabéns! O número que estava pensando era {numero_secreto}')



'''Forma mais aprimorada que limita a quantidade de entradas do usuário:'''

import random

numero_secreto = random.randint(1, 10)
palpite = int(input('Olá jogador(a)! \nTente adivinhar, em 5 tentativas, o número que estou pensando de 1 á 10: '))
tentativas = 4 # o número de tentativas, na verdade, é (tentativas + 1), pois tem o input fora e depois tem dentro do while (pegando a variável tentativas)
vitoria = False

while vitoria == False:
    if palpite < 1 or palpite > 10:
        palpite = int(input('\nEsse número não é válido...\nDigite um número de 1 á 10 para que eu possa adivinhar: '))
        # continue 
    elif palpite != numero_secreto and tentativas > 0:
        tentativas -= 1 
        palpite = int(input('Errou! Tente mais uma vez: '))
        # continue
    elif tentativas == 0 and palpite != numero_secreto:
        print(f'\nQue pena! Você não adivinhou o número que eu estava pensando... o número era {numero_secreto}!')
        break
    elif palpite == numero_secreto:
        vitoria = True
        print(f'\nParabéns! Você adivinhou o número que eu havia pensado. \nObrigada por jogar!\n')

    