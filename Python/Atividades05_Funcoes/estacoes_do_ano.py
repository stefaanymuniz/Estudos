def Estacoes(dia, mes):
    # PRIMAVERA:  21 setembro até 20 dezembro
    if (21 <= dia <= 30 and mes == 9) or (mes == 10) or (mes == 11) or (dia <= 20 and mes == 12): 
        return 'PRIMAVERA'

    # VERÃO:  21 dezembro até 20 março
    elif (21 <= dia <= 31 and mes == 12) or (mes == 1) or (mes == 2) or (dia <= 20 and mes == 3):
        return 'VERAO'

    # OUTONO: 21 março até 20 junho
    elif (21 <= dia <= 31 and mes == 3) or (mes == 4) or (mes == 5) or (dia <= 20 and mes == 6):
        return 'OUTONO'

    # INVERNO: 21 junho até 20 setembro
    elif (21 <= dia <= 30 and mes == 6) or (mes == 7) or (mes == 8) or (dia <= 20 and mes == 9):
        return 'INVERNO'

dia = int(input())
mes = int(input())

print(Estacoes(dia, mes))
