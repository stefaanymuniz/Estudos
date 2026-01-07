carro_veloz = 0
carro_atual = 0
soma_velocidades = 0
quant_velocidades = 0

while True:
    prosseguir = input().lower()
    if prosseguir == 'n':
        break
    ano_carro = int(input())
    velocidade_carro = float(input())
    # Para calcular a média das velocidades cadastradas:
    soma_velocidades += velocidade_carro
    quant_velocidades += 1
    media_velocidades = soma_velocidades/quant_velocidades
    # Atualiza a maior velocidade e o ano do carro mais novo
    if velocidade_carro > carro_veloz:
        carro_veloz = velocidade_carro
    if ano_carro > carro_atual:
        carro_atual = ano_carro

if quant_velocidades == 0:
    print('zero')
else:
    print(f'{carro_veloz:.2f}')
    print(carro_atual)
    print(f'{media_velocidades:.2f}')