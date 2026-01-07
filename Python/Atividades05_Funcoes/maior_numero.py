def MaiorValor(V, W, X, Y, Z):
    maior_num = V
    if W > maior_num:
        maior_num = W
    if X > maior_num:
        maior_num = X
    if Y > maior_num:
        maior_num = Y
    if Z > maior_num:
        maior_num = Z

    return maior_num
    

V = float(input())
W = float(input())
X = float(input())
Y = float(input())
Z = float(input())

print(f'{MaiorValor(V, W, X, Y, Z):.2f}')