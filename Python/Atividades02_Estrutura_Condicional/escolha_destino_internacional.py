estacao = input('Insira a estação desejada: ')
clima = input('Preferência de clima: ')
tipo_destino = input('Preferência por tipo de destino: ')

if estacao == 'verão' and clima == 'quente' and tipo_destino == 'praia':
    print('Brasil (Nordeste)')

elif estacao == 'verão' and clima == 'frio' and tipo_destino == 'cidade':
    print('EUA')

elif estacao == 'inverno' and clima == 'frio' and tipo_destino == 'natureza':
    print('Irlanda')

elif estacao == 'outono' and clima == 'moderado' and tipo_destino == 'cidade':
    print('Espanha')

elif estacao == 'primavera' and clima == 'moderado' and tipo_destino == 'natureza':
    print('Japão (região rural)')

elif estacao == 'primavera' and clima == 'quente' and tipo_destino == 'praia':
    print('Tailândia')

elif estacao == 'outono' and clima == 'quente' and tipo_destino == 'cidade':
    print('Argélia')

elif estacao == 'inverno' and clima == 'quente' and tipo_destino == 'praia':
    print('Austrália')

else:
    print('Não temos uma sugestão para essa combinação')