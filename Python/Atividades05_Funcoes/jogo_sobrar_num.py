def detectarMenorValor():
    global lst_num_quadro
    menor_valor = 999
    indice = 0
    
    for valor in lst_num_quadro:
        if valor < menor_valor:
            menor_valor = valor
            
    for i in range(len(lst_num_quadro)):
        if menor_valor == lst_num_quadro[i]:
            indice = i
            break
            
    return indice
    
def detectarMaiorValor():
    global lst_num_quadro
    maior_valor = 0
    indice = 0
    
    for valor in lst_num_quadro:
        if valor > maior_valor:
            maior_valor = valor
    
    for i in range(len(lst_num_quadro)):
        if maior_valor == lst_num_quadro[i]:
            indice = i
            break
        
    return indice

def partidaJogador01():
    lst_num_quadro.pop(detectarMaiorValor())
        
def partidaJogador02():
    lst_num_quadro.pop(detectarMenorValor())


quant_num = int(input())
lst_num_quadro = [int(x) for x in input().split()]

if len(lst_num_quadro) == 1:
        numero_vencedor = lst_num_quadro[0]
else:
    for i in range(len(lst_num_quadro)):
        partidaJogador01()
        partidaJogador02()

print(numero_vencedor)
    