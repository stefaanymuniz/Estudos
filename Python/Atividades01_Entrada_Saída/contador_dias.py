'''
Faça um algoritmo para entrar com o dia e o mês de uma data e ao final o algoritmo deve informar quantos dias 
se passaram desde o início do ano. Considere sempre que um mês possui 30 dias exatos e que o usuário irá 
passar o mês como um valor inteiro entre 1 e 12.
'''

dia = int(input('Qual dia é hoje? '))
mes = int(input('O mês atual (1 á 12): '))
if 1 <= mes <= 12:
    print('Já se passaram', (mes-1) * 30 + (dia-1), 'dias desde o início do ano.')
else:
    print('\nDigite um número válido de 1 á 12')

# (quantidade de meses - 1) * 30 - (quantidade de dias do mês atual - 1)
# esse "menos 1" em meses é para retirar o mês atual