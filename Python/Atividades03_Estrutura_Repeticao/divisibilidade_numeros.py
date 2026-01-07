''''''

numero = int(input())

for divisores in range (numero,0,-1):
    if numero % divisores == 0:
        print(divisores)