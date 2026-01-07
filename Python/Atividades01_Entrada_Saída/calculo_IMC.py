'''
Faça um programa que receba as características (massa e altura) de 
uma pessoa e retorne seu IMC - Índice de Massa Corporal.
O valor de saída deve ser arredondado usando 2 casas decimais.

A massa em Kg que pode estar entre 1 e 500.
A altura em metros (m) que pode estar entre 1 e 2.8
'''

massa = float(input('Digite sua massa (Kg): '))
altura = 0

if 1 <= massa <= 500:
    altura = float(input('Digite sua altura (m): '))
else:
    print('Digite um valor de massa válido')
 
if 1 <= altura <= 2.8:
    IMC = massa/altura**2   


print('Seu IMC é %.2f' % IMC)
