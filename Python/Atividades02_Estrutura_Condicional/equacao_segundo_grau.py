a = int(input())
b = int(input())
c = int(input())

delta = b**2 - 4*a*c 

if a == 0:
    print('NEESG') # Não é equação 2º grau
elif delta < 0:
    print('NRR') # Não existe raiz real
elif delta == 0: 
    raiz1 = (-b + delta**(1/2))/(2*a)
    print(f'{raiz1:.2f}\n{raiz1:.2f}') # Raízes iguais
elif delta > 0:
    raiz1 = (-b + delta**(1/2))/(2*a)
    raiz2 = (-b - delta**(1/2))/(2*a)
    print(f'{raiz1:.2f}\n{raiz2:.2f}') # Raízes distintas