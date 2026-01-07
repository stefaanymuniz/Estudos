def validar_datas(retirada, devolucao):
    if devolucao > retirada:
        return 'Data de devolucao inferior a data de locacao'
    
def calcular_quant_dias():

def valor_final():
    valor_locacao = (valor_diaria * )

while True:
    modelo_carro = input().upper()

    if modelo_carro == 'FIM':
        break
    elif modelo_carro == 'B':
        valor_diaria = 30.00
    elif modelo_carro == 'I':
        valor_diaria = 40.00
    elif modelo_carro == 'P':
        valor_diaria = 60.00
    else:
        print('Modelo de carro invalido')

    data_retirada = input()
    data_devolucao = input()
    
    valores_odometro = [int(x) for x in input().split()]