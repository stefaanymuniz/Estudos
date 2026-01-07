def ClassificaAluno(media, quant_faltas):
    if quant_faltas > 10:
        return 'REPROVADO POR FALTAS'
    elif media >= 9.5:
        return 'APROVADO COM LOUVOR'
    elif media >= 7:
        return 'APROVADO'
    else:
        return 'REPROVADO'

media = float(input())
quant_faltas = int(input())

resultado = ClassificaAluno(media, quant_faltas)
print(resultado)

'''Jeito que fiz antes:'''

# media = float(input())
# quant_faltas = int(input())


# def ClassificaAluno(media, quant_faltas):
#     if quant_faltas > 10:
#         print('REPROVADO POR FALTAS')
#     elif media < 7:
#         print('REPROVADO')
#     elif media >= 9.5:
#         print('APROVADO COM LOUVOR')
#     elif media >= 7:
#         print('APROVADO')

# ClassificaAluno(media, quant_faltas)