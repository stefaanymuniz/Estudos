# Exercício "Datas entre dias: o retorno" do The Huxley

quant_elementos = int(input())
lista_ordenada = []
lista_resultados = []

lista = [int (x) for x in input().split()]

lista_ordenada = sorted(lista)

for indice in range(quant_elementos):
    if lista[indice] == lista_ordenada[indice]:
        # O índice referenciado na lista (lista_indice) que vai de 0 a quant_elementos
        # e o índice "real" de 1 a quant_elementos
        lista_resultados.append([lista[indice],indice+1])

print(len(lista_resultados))

for i in range(len(lista_resultados)):
    print(lista_resultados[i][0], lista_resultados[i][1])