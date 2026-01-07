def calcula_quadrado(L):
    if L < 0:
        return -1
    else:
        area = L**2
        return area

def calcula_retangulo(B, A):
    if B < 0 or A < 0:
        return -1
    else:
        area = B * A
        return area

def calcula_circulo(r):
    if r < 0:
        return -1
    else:
        pi = 3.14
        area = pi * r**2
        return area


quant_figuras = 0
quant_circulos = 0
areas_quadrados = []
areas_retangulos = []
areas_circulos = []

while True:
    tipo_figura = input()

    if tipo_figura == 'sair':
        break

    if tipo_figura == 'q':
        quant_figuras += 1

        lados = float(input())

        areas_quadrados.append(calcula_quadrado(L = lados))
        # Coloca os resultados da chamada da função dentro da lista vazia e a ordena:
        areas_quad_ordenados = sorted(areas_quadrados, reverse = True)
        maior_area_quad = areas_quad_ordenados[0]

    if tipo_figura == 'r':
        quant_figuras += 1

        base = float(input())
        altura = float(input())

        areas_retangulos.append(calcula_retangulo(B = base, A = altura))
        areas_retan_ordenados = sorted(areas_retangulos, reverse = True)
        maior_area_retan = areas_retan_ordenados[0]

    if tipo_figura == 'c':
        quant_figuras += 1
        quant_circulos += 1

        raio = float(input())

        areas_circulos.append(calcula_circulo(r = raio))
        areas_circ_ordenados = sorted(areas_circulos, reverse = True)
        maior_area_circ = areas_circ_ordenados[0]

percentual_circulos = quant_circulos/quant_figuras * 100

print(f'Maior circulo: {maior_area_circ:.2f}')
print(f'Maior retangulo: {maior_area_retan:.2f}')
print(f'Maior quadrado: {maior_area_quad:.2f}')
print(f'Quantidade de figuras {quant_figuras}')
print(f'Percentual de circulos: {percentual_circulos:.2f}')