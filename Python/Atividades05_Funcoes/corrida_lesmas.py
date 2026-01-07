def calcularNivel(velocidades):
    nivel_mais_veloz = 0

    for velocidade in velocidades:
        
        if velocidade >= 20:
            nivel_veloz = 3
        elif velocidade >= 10 and velocidade < 20:
            nivel_veloz = 2
        elif velocidade < 10:
            nivel_veloz = 1

        # Enquanto o "nivel_veloz" se altera a cada loop, "nivel_mais_veloz" 
        # permanece intacto com o maior nivel que já passou pelo loop
        if nivel_veloz > nivel_mais_veloz:
            nivel_mais_veloz = nivel_veloz
    
    return nivel_mais_veloz


quant_lesmas = int(input())
velocidades_lesmas = [int(x) for x in input().split()]

print(f'Quantidade de lesmas: {quant_lesmas}')
print(f'Lista de velocidades: {velocidades_lesmas}')
print(f'Nível da lesma mais veloz: {calcularNivel(velocidades_lesmas)}')
