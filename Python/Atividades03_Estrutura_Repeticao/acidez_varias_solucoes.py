valor_ph = 0

while True:
    valor_ph = float(input())
    if valor_ph == -1:
        break
    elif valor_ph > 7:
        print('BASICA')
    elif valor_ph < 7:
        print('ACIDA')
    elif valor_ph == 7:
        print('NEUTRA')


# a = 0
# while True:
#     a += 1

#     if a > 10 and a < 20:
#         continue # faz o comando voltar ao início até que o

#     print(a)

#     if a > 50:
#         break