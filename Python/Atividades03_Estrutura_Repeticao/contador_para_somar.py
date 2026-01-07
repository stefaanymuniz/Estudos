'''
Elaborar um programa que solicite ao
usuário oito números inteiros e ao final
apresente a soma desses oito números.
'''

contador = 1
soma = 0

while (contador <= 8):
    soma += int(input('Digite um número: '))
    contador += 1

print(soma)