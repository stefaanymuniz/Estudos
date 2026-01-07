soma_salarios = 0
quant_salarios = 0
maior_salario = 0
pessoas_salario_cem = 0

soma_filhos = 0
total_filhos = 0

while True:
    salario_habitantes = float(input('Digite o seu salário: '))
    if salario_habitantes < 0:
        break
    quant_filhos = int(input('Quantidade de filhos: '))
    # Descobrir média dos filhos
    soma_filhos += quant_filhos
    total_filhos += 1
    # Descobrir média do salário da população
    soma_salarios += salario_habitantes
    quant_salarios += 1
    # Descobrir o maior salário
    if salario_habitantes > maior_salario:
        maior_salario = salario_habitantes
    # Saber quem tem salário de até R$100.00
    if salario_habitantes <= 100.00:
        pessoas_salario_cem += 1

# Verifica se há dados para evitar divisão por zero
if quant_salarios > 0:
    media_salario_populacao = soma_salarios/quant_salarios
    percentual_salario_cem = pessoas_salario_cem/quant_salarios * 100
else:
    media_salario_populacao = 0
    percentual_salario_cem = 0
    
if quant_filhos > 0:
    media_filhos = soma_filhos/total_filhos
else:
    media_filhos = 0


print(f'A média de salário da população é: {media_salario_populacao}')
print(f'A média do número de filhos é: {media_filhos}')
print(f'O maior salário é de R${maior_salario}')
print(f'O percentual de pessoas com salário até R$100,00 é de {percentual_salario_cem}%')