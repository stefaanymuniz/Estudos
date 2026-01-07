nota_final = float(input('Insira sua nota final: '))

if nota_final < 0 or nota_final > 10.0:
    print('Nota inválida. Insira uma nota entre 0.0 e 10.0')

elif 9 <= nota_final <= 10:
    print('Conceito: A')
    print('Situação: Aprovado')

elif 8 <= nota_final <= 8.9:
    print('Conceito: B')
    print('Situação: Aprovado')

elif 6.5 <= nota_final <= 7.9:
    print('Conceito: C')
    print('Situação: Aprovado')

elif 4 <= nota_final <= 6.4:
    print('Conceito: D')
    print('Situação: Reprovado')

elif 0 <= nota_final <= 3.9:
    print('Conceito: F')
    print('Situação: Reprovado')
