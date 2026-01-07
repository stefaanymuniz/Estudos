'''
A Locadora de Veículos Eudora lançou uma grande promoção esse mês:
pagando apenas R$ 90 por diária, o cliente pode alugar um carro de
passeio. Para cada diária, o cliente recebe uma cota de quilometragem
de 100 Km. Cada quilômetro a mais custará uma taxa extra de R$ 12.

Escreva um programa que receba como entrada a quantidade de dias e a
quilometragem total rodada por um cliente dessa locadora e exiba o valor
total a ser pago com duas casas decimais.
'''

dias = int(input())
km_total = int(input())

valor_diaria = dias * 90

if km_total < 100:
    print('%.2f' % valor_diaria)    

elif km_total > 100:
    km_excedidos = km_total - (100 * dias) 
    taxa_extra = km_excedidos * 12
    print('%.2f' % (valor_diaria + taxa_extra))