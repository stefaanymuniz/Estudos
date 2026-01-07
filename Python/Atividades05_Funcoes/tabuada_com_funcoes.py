def multiplicar(num1, num2):
    resultado = num1 * num2
    return resultado


multiplicador = int(input())
resp = 0

for num in range(11):
    resp = multiplicar(num, multiplicador) 
    print('{} x {} = {}'.format(num, multiplicador, resp))
