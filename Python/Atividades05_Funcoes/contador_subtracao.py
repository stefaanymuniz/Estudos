def Subtracao(X, Y):
    quant_subtracao = 0
    while X >= Y:
        X -= Y
        quant_subtracao += 1
    # Outra forma de fazer:
    # while True:
    #     if Y > X:
    #         break
    #     else:
    #         X -= Y
    #         quant_subtracao += 1
    return quant_subtracao


X = int(input())
Y= int(input())

print(Subtracao(X, Y))