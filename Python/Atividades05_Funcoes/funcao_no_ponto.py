def FuncaoPonto(x):
    if x < 1:
        f_x = 4 - x**2
        return f_x
    elif x == 1:
        f_x = 2
        return f_x
    elif x > 1:
        f_x = 2 + x**2
        return f_x

x = int(input())

print(f'f({x}) = {FuncaoPonto(x)}')