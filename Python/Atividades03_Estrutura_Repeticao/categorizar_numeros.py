'''Exercício "Números" do The Huxley'''

valores_pares = 0
valores_impares = 0
valores_positivos = 0
valores_negativos = 0

while True:
    n = int(input())
     
    if n == 0:
        break
    if n % 2 == 0:
        valores_pares += 1
    else:
        valores_impares += 1
    if n > 0:
        valores_positivos += 1
    else:
        valores_negativos += 1

# Jeito mais clean usando o operador ternário:
print(f'{valores_pares} {"valor par" if valores_pares == 1 else "valores pares"}')
print(f'{valores_impares} {"valor ímpar" if valores_impares == 1 else "valores ímpares"}')
print(f'{valores_positivos} {"valor positivo" if valores_positivos == 1 else "valores positivos"}')
print(f'{valores_negativos} {"valor negativo" if valores_negativos == 1 else "valores negativos"}')

# if valores_pares == 1:
#     print(f'{valores_pares} valor par')
# else:
#     print(f'{valores_pares} valores pares')
# if valores_impares == 1:
#     print(f'{valores_impares} valor ímpar')
# else:
#     print(f'{valores_impares} valores impares')
# if valores_positivos == 1:
#     print(f'{valores_positivos} valor positivo')
# else:
#     print(f'{valores_positivos} valores positivos')
# if valores_negativos == 1:
#     print(f'{valores_negativos} valor negativo')
# else:
#     print(f'{valores_negativos} valores negativos')
