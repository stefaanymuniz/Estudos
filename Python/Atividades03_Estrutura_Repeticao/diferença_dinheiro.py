dinheiro_A = 10000.00
fortuna_A = 100.00

dinheiro_B = 5000.00
fortuna_B = 300.00

while dinheiro_A >= dinheiro_B:
    diferenca_salario = dinheiro_A - dinheiro_B
    dinheiro_A += fortuna_A
    dinheiro_B += fortuna_B
    print(f'{diferenca_salario:.2f}')