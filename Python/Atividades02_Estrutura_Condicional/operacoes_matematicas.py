operacoes = input('Selecione as seguintes opções para calcular: somar (S), subtrair(SU), multiplicar (M) e dividir (D): ')

if operacoes == 'S' or operacoes == 'SU' or operacoes == 'M' or operacoes == 'D':
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))

if operacoes == 'S':
    r = n1 + n2
    print('A soma é', r)

elif operacoes == 'SU':
    r = n1 - n2
    print('A subtração é', r)

elif operacoes == 'M':
    r = n1 * n2
    print('A multiplicação é', r)

elif operacoes == 'D':
    r = n1 / n2
    print('A divisão é', r)

else:
    print('Opção Inválida')