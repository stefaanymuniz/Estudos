def velkmh(Vo, A, T):
    velocidade_final = (Vo + A * T) * 3.6 # Vo em m/s para V em km/h
    return velocidade_final

velocidades = [] # Lista para armazenar as velocidades finais dos três carros

for _ in range(3):
    velocidade_inicial = float(input())
    aceleracao = float(input())
    tempo_de_percurso = float(input())

    # Calcula a velocidade final e adiciona à lista
    velocidade_carros = velkmh(velocidade_inicial, aceleracao, tempo_de_percurso)
    velocidades.append(velocidade_carros)

# Para encontrar a menor velocidade
menor_velocidade = min(velocidades)

print(menor_velocidade)

