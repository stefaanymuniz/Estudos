# Exercício "Intercalar um array" do The Huxley

tam_arrays = int(input())
array_completo = []

for i in range(tam_arrays*2):
    valores = int(input())
    array_completo.append(valores)

meio = len(array_completo)//2

primeira_parte = array_completo[:meio]
segunda_parte = array_completo[meio:]

for i in range(len(primeira_parte)):
    print(primeira_parte[i])
    print(segunda_parte[i])