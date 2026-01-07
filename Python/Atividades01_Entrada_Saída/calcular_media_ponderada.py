'''
A partir de três notas de um estudante, prepare um programa
para “Calcular Média com Pesos”, capaz de calcular a média final
com pesos de notas 20%, 30% e 50%, respectivamente. Ao final, o 
programa deve imprimir o nome do aluno, suas notas parciais e sua média final.
'''

print('Calculadora Médias com Pesos')
nome=input('Nome do aluno: ')
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
media = (n1 * 0.2) + (n2 * 0.3) + (n3 * 0.5)
print('\nNome: ', nome, 
      '\nNotas Parciais: '
      '\nPrimeira Nota: ', n1,
      '\nSegunda Nota: ', n2,
      '\nTerceira Nota: ', n3,
      '\nMédia Final: ', round(media, 2))

# print(f'\nNome: {nome}\nNotas Parciais: \nPrimeira Nota: {n1}\nSegunda Nota: {n2}\nTerceira Nota: {n3}\nMédia Final: {round(media, 2)}')
