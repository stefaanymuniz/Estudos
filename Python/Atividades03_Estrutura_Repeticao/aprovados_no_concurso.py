aprovado = 0
quant_aprovados = 0

while True:
    questoes_portugues = int(input())
    if questoes_portugues < 0:
        break
    questoes_matematica = int(input())
    nota_redacao = float(input())
    aprovado = 0
    if questoes_portugues >= 40:
        aprovado += 1
    if questoes_matematica >= 21:
        aprovado += 1
    if nota_redacao >= 7.0:
        aprovado += 1
    if aprovado == 3:
        quant_aprovados += 1
        continue
    elif aprovado < 3:
        continue
print(quant_aprovados)
    
# se a pessoa tiver número 3 em (aprovados) ela é contabilizada que passou em quant_aprovados