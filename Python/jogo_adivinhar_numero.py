import random

palpite = int(input('Olá jogador(a)! Tente adivinhar o número que estou pensando: '))
numero_secreto = random.randint(1, 10)

while palpite != numero_secreto:
  palpite = int(input('Errou! Tente mais uma vez: '))

print(f'Parabéns! O número que estava pensando era {numero_secreto}')   