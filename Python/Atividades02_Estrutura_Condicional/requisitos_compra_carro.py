'''
O professor Henrique deseja trocar de carro e precisa que o carro que ele vai
comprar tenha a melhor relação custo-benefício possível. No entanto, Henrique
gostaria que certas características fossem respeitadas. Algumas delas são
obrigatórias, outras são desejáveis.

Obrigatórias:
Deve ter amplo espaço interno
Deve ter porta-malas grande

Desejáveis:
Custar abaixo de R$ 100.000,00
Motor 1.5 ou superior
Ter câmbio automático
'''

espaco_interno = input()
porta_malas = input()
valor_carro = float(input())
motor = float(input())
cambio = input()

if espaco_interno == 'C' or porta_malas == 'P': # Se não atender os requisitos obrigatórios
    print('Não compre!')

elif valor_carro < 100000 and motor >= 1.5 and cambio == 'A': # Se atender todos os requisitos desejáveis
    print('Pode comprar!')

elif (valor_carro < 100000 and motor >= 1.5) or (valor_carro < 100000 and cambio == 'A') or (motor >= 1.5 and cambio == 'A'): # 2 requisitos
    print('Boa compra.')

elif valor_carro < 100000 or motor >= 1.5 or cambio == 'A': # 1 requisito
    print('Pode ser uma opção.')

else: # Nenhum requisito desejável
    print('Recomendo pensar melhor...')