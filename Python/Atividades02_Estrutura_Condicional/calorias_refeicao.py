'''
Criar um programa que informe a quantidade total de calorias de 
refeição a partir do usuário que deverá informar o prato, a
sobremesa e a bebida.
'''
# Calorias:
# Prato          
vegetariano = 180
peixe = 230
frango = 250
carne = 350
# Sobremesas
abacaxi = 75
sorvete_diet = 110
mousse_diet = 170
mousse_chocolate = 200
# Bebidas
cha = 20
suco_laranja = 70
suco_acerola = 100
refrigerante = 300

prato = input('Selecione um prato: ')
sobremesa = input()
bebida = input()
opcao_valida = True

calorias_totais = 0

if prato != 'Vegetariano' and prato != 'Peixe' and prato != 'Frango' and prato != 'Carne' or\
   sobremesa != 'Abacaxi' and sobremesa != 'Sorvete Diet' and sobremesa != 'Mousse Diet' and sobremesa != 'Mousse de Chocolate' or\
   bebida != 'Chá' and bebida != 'Suco de Laranja' and bebida != 'Suco de Acerola' and bebida != 'Refrigerante':
    print('Selecione uma opção válida')
    opcao_valida = False

if opcao_valida == True:
    if prato == 'Vegetariano':
        calorias_totais += vegetariano # mesma coisa de fazer calorias_totais = calorias_totais + vegetariano
    elif prato == 'Peixe':
        calorias_totais += peixe
    elif prato == 'Frango':
        calorias_totais += frango
    elif prato == 'Carne':
        calorias_totais += carne    

    if sobremesa == 'Abacaxi':
        calorias_totais += abacaxi
    elif sobremesa == 'Sorvete Diet':
        calorias_totais += sorvete_diet
    elif sobremesa == 'Mousse Diet':
        calorias_totais += mousse_diet
    elif sobremesa == 'Mousse de Chocolate':
        calorias_totais += mousse_chocolate

    if bebida == 'Chá':
        calorias_totais += cha
    elif bebida == 'Suco de Laranja':
        calorias_totais += suco_laranja
    elif bebida == 'Suco de Acerola':
        calorias_totais += suco_acerola
    elif bebida == 'Refrigerante':
        calorias_totais += refrigerante

    print(f'O total de calorias da sua comida foi de {calorias_totais}')