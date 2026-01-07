'''
Escreva um programa de ajuda para vendedores. A partir do valor do produto digitado pelo usuário, mostre:
• o total a pagar com desconto de 10%
• o valor de cada parcela, no parcelamento de 3× sem juros;
• a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)
• a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)
'''

valor_total = int(input('Digite o valor total do produto: '))
valor_desconto = (valor_total * 90)/100

print('A vista com desconto de 10%%: %.2f' % valor_desconto)
print('Valor da parcela em 3x sem juros: %.2f' % (valor_total/3))
print('Comissao do vendedor a vista: %.2f' % ((valor_desconto * 5)/100))
print('Comissao do vendedor a prazo: %.2f' % ((valor_total * 5)/100))