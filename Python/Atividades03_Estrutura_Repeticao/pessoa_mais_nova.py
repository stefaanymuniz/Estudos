'''Leia o nome e a idade de 10 pessoas e exiba o nome da pessoa mais nova.'''

pessoa_mais_nova = ''
idade_mais_nova = 999 # valor alto só para a primeira entrada ser validada

# a variável não é importante, apenas a quantidade de repetições, por isso o "_"
for _ in range(10): # range(10) -> sequência de 0 á 9, ou seja, 10 números
    nome = input()
    idade = int(input())
    if idade < idade_mais_nova:
        pessoa_mais_nova = nome
        idade_mais_nova = idade

print(pessoa_mais_nova)
