def FormamRetangulo(a, b, c, d):
    if (a == c and b == d) or (a == b and c == d) or (a == d or b == c):
        return 'formam um retangulo'
    else:
        return 'nao formam um retangulo'

a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(FormamRetangulo(a, b, c, d))