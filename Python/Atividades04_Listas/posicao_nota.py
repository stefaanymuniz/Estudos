# Exercício "Listas - exibindo nota e posição" do The Huxley

quant_notas = int(input())
soma_notas = 0
notas = []

if quant_notas <= 0 or quant_notas > 5:
    print('Numero de notas invalido.')
else:
    for i in range(quant_notas):
        nota = float(input())
        soma_notas += nota
        notas.append(nota)

    media = soma_notas/quant_notas

    for i in range(1, quant_notas + 1):
        print(f'Nota {i}: {notas[i-1]}')
    print(f'Media: {media:.2f}')