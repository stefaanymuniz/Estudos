'''
Um motorista deseja abastecer seu carro. Escreva um programa para ler o preço do litro da gasolina e 
o valor do pagamento, e exibir quantos litros ele conseguiu colocar no tanque.
'''

gas = float(input('Digite o preço da gasolina: '))
pagamento = float(input('Digite o valor do pagamento: '))
litros = pagamento/gas
print('Você colocou', round(litros), 'litros de gasolina.')