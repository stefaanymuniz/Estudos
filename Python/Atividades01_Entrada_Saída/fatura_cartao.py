'''
Uma administradora de cartões está oferecendo uma promoção aos seus clientes. 
A pessoa que não puder pagar o total da fatura no mês de março poderá pagar 
apenas 50% do valor, e o restante poderá ser pago no mês seguinte com juros de 6,5%. 

Desenvolva uma solução para ajudar o cliente a descobrir qual será o valor de sua 
fatura no mês de abril caso ele aceite a proposta. 
'''

fatura_marco = float(input())
nova_fatu_marco = (fatura_marco * 50)/100
fatura_abril = (fatura_marco - nova_fatu_marco) * (1 + 0.065)

print('Valor total da fatura: R$ %.2f' % fatura_marco)
print('Valor a pagar em Marco: R$ %.2f' % nova_fatu_marco)
print('Valor a pagar em Abril: R$ %.2f' % fatura_abril)