consoantes = 0
todas_palavras = []
vogal = ['a', 'e', 'i', 'o', 'u']
mais_consoantes = 0

while True:
    entrada = input()

    if entrada == 'FIM':
        break
    else:
        palavras_linha = entrada.split()
        todas_palavras.extend(palavras_linha)

if todas_palavras == []:
    print('texto vazio')
else:
    palavra_mais_consoante = todas_palavras[0]
    for palavra in todas_palavras:

        for caractere in palavra:
            if caractere.isalpha() and (caractere.lower() not in vogal):
                consoantes += 1

        if consoantes > mais_consoantes:
            mais_consoantes = consoantes
            palavra_mais_consoante = palavra
                
        consoantes = 0
          
    print(palavra_mais_consoante)