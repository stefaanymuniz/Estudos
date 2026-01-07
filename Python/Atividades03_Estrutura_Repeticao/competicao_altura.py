'''Os primos Huguinho e Zezinho vivem competindo em diversas coisas.
Uma das coisas é a altura, pois Huguinho é mais alto que Zezinho atualmente. 

Sabendo que Huguinho cresce 2 centímetros por ano e Zezinho cresce 3
centímetros por ano, então Zezinho desafiou Huguinho dizendo que em alguns 
anos ele irá ser mais alto que ele. 

Construa um algoritmo que calcule e imprima quantos anos serão necessários
para que Zezinho seja maior que Huguinho.'''

altura_atual_huguinho = int(input())
altura_atual_zezinho = int(input())
anos = 0

while altura_atual_huguinho >= altura_atual_zezinho:
    altura_atual_huguinho += 2
    altura_atual_zezinho += 3
    anos += 1

print(f'Serão necessários {anos} anos para Zezinho ser mais alto que Huguinho.')