'''Janaína, estudante de Engenharia de Materiais, precisa calcular o
resultado de x ao quadrado menos quatro x mais cinco (x**2 - 4*x + 5).
Só que ela precisa calcular o resultado dessa fórmula para vários
valores de x dentro de um determinado intervalo.'''

numero_a = int(input())
numero_b = int(input())

for x in range(numero_a, numero_b + 1):
    resultados = x**2 - 4 * x + 5
    print(resultados)