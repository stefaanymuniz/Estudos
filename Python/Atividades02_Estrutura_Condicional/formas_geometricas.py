from unidecode import unidecode # Para remover os acentos

forma_geometrica = input()

if unidecode(forma_geometrica).lower() == 'retangulo':
    base = float(input())
    altura = float(input())
    area = base * altura
    print(f'{area:.2f}')

elif unidecode(forma_geometrica).lower() == 'triangulo':
    base = float(input())
    altura = float(input())
    area = (base * altura)/2
    print(f'{area:.2f}')
    
elif unidecode(forma_geometrica).lower() == 'trapezio':
    base_maior = float(input())
    base_menor = float(input())
    altura = float(input())
    area = ((base_maior + base_menor) * altura)/2
    print(f'{area:.2f}')

elif unidecode(forma_geometrica).lower() == 'circulo':
    raio = float(input())
    area = 3.1415 * raio**2
    print(f'{area:.2f}')

else:
    print('Figura invalida.')