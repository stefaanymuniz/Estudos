'''
Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas
efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão
sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas
decimais. 
'''

nome_vendedor = input('Digite seu nome: ')
salario_fixo = float(input('Digite seu salário fixo: R$'))
total_vendas = float(input('Total de vendas no mês: R$'))

comissao = total_vendas * 0.15
valor_total = salario_fixo + comissao

print('TOTAL = R$ %.2f' % valor_total)