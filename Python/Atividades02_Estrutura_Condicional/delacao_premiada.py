# Exercício "Delação Premiada" do The Huxley

crime_delator = input()
crime_valido = True

if crime_delator != 'roubo' and crime_delator != 'tráfico' and crime_delator != 'homicídio':
    crime_valido = False
    print('Crime inválido.')
elif crime_delator == 'roubo' or crime_delator == 'tráfico':
    valor_crime_delator = float(input())

if crime_valido == True:
    crime_delatado = input()
    
    if crime_delatado != 'roubo' and crime_delatado != 'tráfico' and crime_delatado != 'homicídio':
        crime_valido = False
        print('Crime inválido.')
    elif crime_delatado == 'roubo' or crime_delatado == 'tráfico':
        valor_crime_delatado = float(input())

    if crime_valido == True:
    
        # Crime do delator for de roubo ou tráfico e o crime delatado for de homicídio
        if (crime_delator == 'roubo' or crime_delator == 'tráfico') and (crime_delatado == 'homicídio'):
            print('Delação concedida.')

        # Crime do delator e o crime delatado são de roubo e o valor do roubo delatado é 5 vezes maior que o do roubo do delator
        elif (crime_delator == 'roubo' and crime_delatado == 'roubo') and (valor_crime_delatado > 5 * valor_crime_delator):
            print('Delação concedida.')

        # Crime do delator é roubo e o crime delatado é tráfico e o valor da droga traficada for mais de 3 vezes maior que o do roubo
        elif (crime_delator == 'roubo' and crime_delatado == 'tráfico') and (valor_crime_delatado > 3 * valor_crime_delator):
            print('Delação concedida.')

        # Crime do delator e o crime delatado são de tráfico e o valor da droga traficada for mais de 5 vezes maior que o do tráfico do delator
        elif (crime_delator == 'tráfico' and crime_delatado == 'tráfico') and (valor_crime_delatado >  5 * valor_crime_delator):
            print('Delação concedida.')

        # Caso do delator ter cometido um homicídio e quiser delatar um homicídio
        elif crime_delator == 'homicídio' and crime_delatado == 'homicídio':
            print('Delação concedida.')

        else:
            print('Delação rejeitada.')