'''
Faça um programa que calcule o IMC de uma
pessoa (IMC = massa em kg / altura em metros
elevado ao quadrado) e informe a sua classificação
segundo a tabela a seguir:

 IMC           Classificação
< 18,5       Abaixo do Peso
18,6 - 24,9  Saudável
25,0 - 29,9  Peso em excesso
30,0 - 34,9  Obesidade Grau I
35,0 - 39,9  Obesidade Grau II (severa)
≥ 40,0       Obesidade Grau III (mórbida)
'''

import math

massa = float(input('Informe seu peso (Kg): '))
altura = float(input('Informe sua altura: '))

imc = math.ceil(massa/altura**2) # Arredondar para cima

print(imc)

if imc < 18.5:
    print('Você está abaixo do peso')
elif 18.6 <= imc <= 24.9:
    print('Você está saudável')
elif 25.0 <= imc <= 29.9:
    print('Você está com Peso em excesso')
elif 30.0 <= imc <= 34.9:
    print('Você está com Obesidade Grau I')
elif 35.0 <= imc <= 39.9:
    print('Você está com Obesidade Grau II (Severa)')
elif imc >= 40.0:
    print('Você está com Obesidade Grau III (Mórbido)')

else:
    print('Opção Inválida')
    