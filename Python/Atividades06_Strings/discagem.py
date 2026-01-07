teclas = [['A', 'B', 'C'], \
         ['D', 'E', 'F'], \
         ['G', 'H', 'I'], \
         ['J', 'K', 'L'], \
         ['M', 'N', 'O'], \
         ['P', 'Q', 'R', 'S'], \
         ['T', 'U', 'V'], \
         ['W', 'Y', 'Z']]
numeros = ['0','1','2','3','4','5','6','7','8','9']

num_telefone = input()

num_sem_hifen = num_telefone.split('-')
num_traduzido = []

for num in num_sem_hifen:
    for caracteres in num:
        
        if caracteres in numeros:
            num_traduzido.append(caracteres)
        else:
            if caracteres in teclas[0]:
                num_traduzido.append(2)
            elif caracteres in teclas[1]:
                num_traduzido.append(3)
            elif caracteres in teclas[2]:
                num_traduzido.append(4)
            elif caracteres in teclas[3]:
                num_traduzido.append(5)
            elif caracteres in teclas[4]:
                num_traduzido.append(6)
            elif caracteres in teclas[5]:
                num_traduzido.append(7)
            elif caracteres in teclas[6]:
                num_traduzido.append(8)
            elif caracteres in teclas[7]:
                num_traduzido.append(9)
    num_traduzido.append('-')

num_traduzido.pop()

for i in num_traduzido:
    print(i, end='')
            