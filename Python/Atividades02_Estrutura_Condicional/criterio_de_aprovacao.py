'''
Escreva um programa que receba as notas e a presença de um aluno,
calcule a média e imprima a situação final do aluno.

No semestre são feitas 3 provas, e faz-se a média ponderada com
pesos 2, 2 e 3, respectivamente.

Os critérios para aprovação são:
1 - Frequência mínima de 75%.
2 - Média final mínina de 6.0 (calculada com uma casa de precisão).

E devem ser considerados os casos especiais descritos para a impressão
dos resultados, com uma mensagem personalizada para cada situação.
'''

n1 = float(input())
n2 = float(input())
n3 = float(input())
frequencia = float(input())

media = round((n1 * 2 + n2 * 2 + n3 * 3)/7, 1)

print(f'Frequencia: {int(frequencia *100)}%')
print(f'Media: {media}')

if frequencia < 0.75:
    print('Aluno reprovado por faltas!')
elif media > 9:
    print('Aluno aprovado com louvor!')
elif 6 <= media <= 9:
    print('Aluno aprovado!')
elif 4 <= media < 6:
    print('Aluno de rec!')
elif media < 4:
    print('Aluno reprovado!')
    