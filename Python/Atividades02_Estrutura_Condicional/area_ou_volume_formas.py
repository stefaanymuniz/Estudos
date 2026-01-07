# Exercício "Área e Volume de Corpos Sólidos" do The Huxley

PI = 3.1415
forma_geometrica = input()

if forma_geometrica != 'c' and forma_geometrica != 'e':
    print(f'Entrada invalida! Voce deve usar \'c\' (cilindro) ou \'e\' (esfera).')
else:
    area_ou_volume = input()

    if area_ou_volume != 'a' and area_ou_volume != 'v':
        print('Entrada invalida! Entre com \'a\' (area) ou \'v\' (volume).')

    elif forma_geometrica == 'c':
        raio = float(input())
        altura = float(input())
        if area_ou_volume == 'a':
            area = 2 * PI * raio * (raio + altura)
            print(f'A area do cilindro de raio {raio:.2f} e altura {altura:.2f} eh:\n{area:.2f}')
        elif area_ou_volume == 'v':
            volume = PI * (raio)**2 * altura
            print(f'O volume do cilindro de raio {raio:.2f} e altura {altura:.2f} eh:\n{volume:.2f}')

    elif forma_geometrica == 'e':
        raio = float(input())
        if area_ou_volume == 'a':
            area = 4 * PI * raio**2
            print(f'A area da esfera de raio {raio:.2f} eh:\n{area:.2f}')
        elif area_ou_volume == 'v':
            volume = (4/3) * PI * (raio)**3
            print(f'O volume da esfera de raio {raio:.2f} eh:\n{volume:.2f}')