'''
José está prestes a inaugurar seu supermercado. Ele acredita que o cidadão
brasileiro é capaz de pagar suas compras sozinho, sem precisar de um funcionário
para conferir se o que ele está pagando corresponde aos produtos que ele está levando. 
Para isso ele vai precisar de um programa que irá ler o dia da semana, o preço
do produto, a opção do produto ("prata" ou "ouro") e o nome. 

Se a compra estiver sendo realizada na segunda, terça ou quarta e a opção do
produto for "ouro", o preço do produto ficará pela metade. 

Se a compra estiver sendo realizada na quinta ou sexta e o preço estiver entre
R$ 10.00 e R$ 100.00, o preço será reduzido para um terço do valor original.

Se a compra estiver sendo realizada no sábado e a opção for prata, o preço do produto será o triplo.
Em qualquer outro caso, o preço será o dobro.
'''

dia_semana = input()
preco = float(input())
opcao_produto = input()
nome_produto = input()

if (dia_semana == 'seg' or dia_semana == 'ter' or dia_semana == 'qua') and opcao_produto == 'ouro':
    novo_preco = preco / 2
elif (dia_semana == 'qui' or dia_semana == 'sex') and 10 <= preco <= 100:
    novo_preco = preco / 3
elif dia_semana == 'sab' and opcao_produto == 'prata':
    novo_preco = preco * 3
else:
    novo_preco = preco * 2

print(f'O preco do produto {nome_produto} no dia {dia_semana} eh {novo_preco:.2f}')
# forma que tava fazendo antes: print('O preco do produto', nome_produto,'no dia', dia_semana, 'eh %.2f' % novo_preco)
