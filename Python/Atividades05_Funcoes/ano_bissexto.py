def contaDigitos(ano):
    if ano < 1000:
        return 'Ano invalido'
    else:
        return True

def ehBissexto(ano):
    if (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0): 
        return True
    else:
        return False

def Mensagem(ano):
    ano_atual = 2020

    if ehBissexto(ano) == True:
        if ano == ano_atual:
            return f'O ano {ano} eh bissexto'
        elif ano < ano_atual:
            return f'O ano {ano} foi bissexto'
        else:
            return f'O ano {ano} serah bissexto'
    else:
        return f'O ano {ano} NAO eh bissexto'


anos = [int(x) for x in input().split()]

for ano in anos:
    if contaDigitos(ano) == True:
        print(Mensagem(ano))
    else:
        print(contaDigitos(ano))