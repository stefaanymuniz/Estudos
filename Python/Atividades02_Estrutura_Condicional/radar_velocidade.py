# Exercício "Devagar, devagar, olhe o radar!!" do The Huxley

velocidade_max = int(input())
velocidade_veiculo = float(input())

velocidade_20 = velocidade_max + velocidade_max * 0.2
velocidade_50 = velocidade_max + velocidade_max * 0.5 

if velocidade_veiculo <= velocidade_max:
    print(f'{0:.2f}')
    print(0)

elif velocidade_veiculo <= velocidade_20:
    multa = 85.13
    pontos_carteira = 4
    print(f'{multa:.2f}\n{pontos_carteira}')

elif velocidade_veiculo > velocidade_20 and velocidade_veiculo <= velocidade_50:
    multa = 127.69
    pontos_carteira = 5
    print(f'{multa:.2f}\n{pontos_carteira}')

elif velocidade_veiculo > velocidade_50:
    multa = 574.62
    pontos_carteira = 7
    print(f'{multa:.2f}\n{pontos_carteira}')