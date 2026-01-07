'''Para descobrir quantos divisores um número possui:'''

numero = int(input('Digite um número para descobrir seus divisores: '))
quant_divisores = 0

for divisores in range(1, numero + 1):
    if numero % divisores == 0:
        quant_divisores += 1
        print(divisores)
print(f'O número {numero} possui {quant_divisores} divisores.')