# Exercício "Múltiplos de N num Intervalo" do The Huxley

n = int(input())
a = int(input())
b = int(input())

tem_multiplo = False

for i in range(a, b + 1):
    if i % n == 0:
        print(i)
        tem_multiplo = True

if tem_multiplo == False:
    print('INEXISTENTE')