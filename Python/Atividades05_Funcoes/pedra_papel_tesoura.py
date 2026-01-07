def vencedor(miguel, maria):
    if miguel > maria:
        return 'MIGUEL'
    else:
        return 'MARIA'
    

quant_rodadas = 0
pontos_miguel = 0
pontos_maria = 0

while quant_rodadas < 5:
    decisao_maria = input().lower()
    decisao_miguel = input().lower()

    # Caso haja empate, a rodada não é considerada
    if decisao_miguel == decisao_maria:
        quant_rodadas += 0
    # Casos em que Miguel ganhe
    elif (decisao_miguel == 'papel' and decisao_maria == 'pedra') or \
        (decisao_miguel == 'pedra' and decisao_maria == 'tesoura') or \
        (decisao_miguel == 'tesoura' and decisao_maria == 'papel'):
        quant_rodadas += 1
        pontos_miguel += 1
    # Caso Miguel não ganhe em nenhum circunstância, quem ganha é Maria
    else:
        quant_rodadas += 1
        pontos_maria += 1


print(vencedor(miguel = pontos_miguel, maria = pontos_maria))
    