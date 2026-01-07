# Exercício "Categorias de nadadores." do The Huxley

idade_nadador = int(input())

if idade_nadador <= 4:
    print('Idade invalida.')
elif 5 <= idade_nadador <= 7:
    print('Infantil A')
elif 8 <= idade_nadador <= 10:
    print('Infantil B')
elif 11 <= idade_nadador <= 13:
    print('Juvenil A')
elif 14 <= idade_nadador <= 17:
    print('Juvenil B')
elif 18 <= idade_nadador <= 40:
    print('Adulto')
elif idade_nadador > 41:
    print('Master')