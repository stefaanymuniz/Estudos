# Exercício "Seleção Brasileira" do The Huxley

quant_titulares = 0
idade_mais_novo = 999
idade_mais_velho = 0 
soma_idades = 0

while quant_titulares < 11:
    nome_jogador = input()

    if nome_jogador == 'sair':
        break

    idade = int(input())
    posicao_jogador = input()

    if idade < idade_mais_novo:
        idade_mais_novo = idade
        jogador_jovem = nome_jogador
        
    if idade > idade_mais_velho:
        idade_mais_velho = idade
        jogador_velho = posicao_jogador

    soma_idades += idade
    quant_titulares += 1

media_idade = soma_idades/quant_titulares

print(f'{jogador_jovem}')
print(f'{jogador_velho}')
print(f'{media_idade:.1f}')