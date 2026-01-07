'''Exercício "Vamos combinar strings?" do The Huxley'''

quant_teste = int(input())

for i in range(quant_teste):
    texto = input().split()
    palavra1 = texto[0]
    palavra2 = texto[1]

    if len(palavra1) < len(palavra2):
        palavra_menor = len(palavra1)
    else: 
        palavra_menor = len(palavra2)

    for caracteres in range(palavra_menor):
        print(palavra1[caracteres], end ='')
        print(palavra2[caracteres], end ='')

    # Continua da onde o loop parou para completar a maior palavra
    print(palavra1[palavra_menor:], end='')
    print(palavra2[palavra_menor:], end='')
    print()