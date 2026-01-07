'''
Escreva um programa que realize a conversão de dólar para real: para cada valor
 lido em dólar da entrada padrão, será exibido o correspondente em reais (1 dólar = 3.55 reais).
'''

valor_dolar = float(input())
valor_real = valor_dolar * 3.55

print('%.2f' % valor_real)