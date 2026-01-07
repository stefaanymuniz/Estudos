'''
Faça um programa para converter um valor de temperatura em uma escala de mediada definida pelo usuário para as outras escalas de medida.

Se o usuário fornecer uma temperatura em graus Celsius, imprima a mesma temperatura em Fahrenheit e Kelvin
Se o usuário fornecer uma temperatura em graus Fahrenheit, imprima a mesma temperatura em Celsius e Kelvin
Se o usuário fornecer uma temperatura em graus Kelvin, imprima a mesma temperatura em Fahrenheit e Celsius
'''

tipo_graus = input()
valor_temp = float(input())

if tipo_graus == 'C' and valor_temp >= -273.15:
    f = 1.8 * valor_temp + 32
    k = valor_temp + 273.15
    print('%.2f' % f, 'F')
    print('%.2f' % k, 'K')

elif tipo_graus == 'F' and valor_temp >= -459.67:
    c = (valor_temp - 32) * 5/9
    k = (valor_temp - 32) * 5/9 + 273.15
    print('%.2f' % c, 'C')
    print('%.2f' % k, 'K')

elif tipo_graus == 'K' and valor_temp >= 0.0:
    c = valor_temp - 273.15
    f = (valor_temp - 273.15) * 9/5 + 32
    print('%.2f' % c, 'C')
    print('%.2f' % f, 'F')

else:
    print('Valor de temperatura abaixo do minimo')

