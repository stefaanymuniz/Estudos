valores = []
quant_elementos = int(input())

if quant_elementos == 0:
    print(valores)
    print('A lista estah vazia - nao eh possivel remover elemento')
else:
    for _ in range(quant_elementos):
        valores.append(int(input()))

    copia_valores = valores[:]
    remover_valor = int(input())

    if remover_valor in valores:
        valores.remove(remover_valor)
        print(copia_valores)
        print(valores)
    else:
        print(f'[ {" ".join(map(str, copia_valores))} ]')
        print(f'[ {' '.join(map(str, copia_valores))} ]') 
        print(f'Nao eh possivel remover o elemento {remover_valor}')
