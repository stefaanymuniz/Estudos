while True:
    numero = int(input())
    quant_divisores = 0 # para definir a variável e resetar para o próximo número
    if numero == -1:
        break
    for divisores in range(1, numero + 1):
        if numero % divisores == 0:
            quant_divisores += 1
            continue
    # Número primos tem >exatamente< dois divisores possíveis, mais do que isso, não é primo, logo:
    if quant_divisores == 2: 
        print('1') # É um número primo
        continue
    else:
        print('0') # Não é um número primo
        continue

# ANOTAÇÕES:
# quant_divisores = numero % divisores == 0

# numeros primos >somente< dão resto '0' se dividir por 1 ou ele mesmo
# outros números até podem ser divisíveis por 1 ou ele mesmo, mas tem mais divisores além desse