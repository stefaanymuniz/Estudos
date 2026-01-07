quant_testes = int(input())

for i in range(quant_testes):
    # Exemplo: NAM SOG -> MANGOS
    string_embaralhada = input()

    metade_string = len(string_embaralhada)//2
    string_invertida01 = string_embaralhada[:metade_string]
    string_invertida02 = string_embaralhada[metade_string:]

    string_normal01 = string_invertida01[::-1]
    string_normal02 = string_invertida02[::-1]

    print(string_normal01 + string_normal02)