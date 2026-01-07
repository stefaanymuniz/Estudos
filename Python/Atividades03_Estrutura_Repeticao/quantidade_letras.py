palavras = input('Digite uma palavra: ').replace(' ', '') # "Quando encontrar um espaço (' '), substitua-o por nada ('')."
contador = 0

for letras in palavras:
    contador += 1

print(f'A sua palavra contém {contador} letras')