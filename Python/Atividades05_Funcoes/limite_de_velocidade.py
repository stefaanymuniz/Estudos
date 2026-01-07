def CalculaMulta(velocidade):
    velocidade_permitida = 50
    multa = 0
    if velocidade <= 50: # se respeitar o limite de velocidade
        multa = 0
        return multa
    elif velocidade <= 55: # no máximo 10% acima da velocidade limite
        multa = 230
        return multa
    elif velocidade <= 60: # exceder a velocidade permitida em até 20%
        multa = 340
        return multa
    elif velocidade > 60: # velocidade do motorista exceda o limite em mais de 20%
        multa = (velocidade - velocidade_permitida) * 19.28 # multa de R$ 19,28 por cada km excedido
        return multa


velocidade = int(input())

print(f'{CalculaMulta(velocidade):.2f}')
