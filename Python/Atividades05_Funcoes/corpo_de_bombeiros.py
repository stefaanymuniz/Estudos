def eventoMudanca(andar, atualizar_moradores):
    # Quant de moradores no andar específico que quer atualizar
    if andar > len(moradores_cada_andar):
        print('nao existe esse andar no predio')
    else:
        moradores_cada_andar[andar - 1] = atualizar_moradores

def eventoChegada(n):
    # Total de pessoas que moram do andar 1 até o andar n, inclusive
    total_moradores = 0

    if n > len(moradores_cada_andar):
        return 'nao existe esse andar no predio'
    else:
        for i in range(n):
            total_moradores += moradores_cada_andar[i]
        return total_moradores 


quant_andares, quant_eventos = [int(x) for x in input().split()]
moradores_cada_andar = [int (x) for x in input().split()]

for i in range(quant_eventos):
    info_evento = [int(x) for x in input().split()]
    tipo_evento = info_evento[0]
    andar = info_evento[1]

    if tipo_evento == 0:
        atualizar_moradores = info_evento[2]
        eventoMudanca(andar, atualizar_moradores)
    elif tipo_evento == 1: # Evento da chegada do bombeiro
        print(eventoChegada(andar))