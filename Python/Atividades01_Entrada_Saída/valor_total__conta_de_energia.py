'''
A conta de energia elétrica de uma determinada cidade é composta por um valor que depende da 
quantidade de energia elétrica usada no mês e uma taxa de iluminação pública de 5% do valor pago 
pela energia. O preço de cada KWh depende da bandeira utilizada, que varia de acordo com a época 
do ano e do histórico de chuvas. 

No momento, a bandeira verde está sendo utilizada e o valor do KWh é de R$ 0,75.

Diante do contexto, você deve desenvolver uma solução para ajudar o consumidor dessa cidade a saber 
quanto será o valor total de sua conta de energia a partir da informação do consumo em KWh, 
informando também o valor a ser pago pela taxa de iluminação pública.
'''

consumo_kwh = float(input('Digite o valor do seu consumo (KWh): '))
pagar_consumo = consumo_kwh * 0.75
iluminacao = pagar_consumo * 0.05
valor_total = pagar_consumo + iluminacao

print('Valor do consumo: R$', pagar_consumo)
print('Valor taxa iluminacao: R$', iluminacao)
print('Valor total a pagar: R$', valor_total)