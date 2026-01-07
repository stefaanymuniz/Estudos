'''Exercíio "Mais uma série" do The Huxley'''

n = int(input())
soma = n/(2*4)
x = 2
y = 4

while n >= 1:
    sequencia = (n-1)/((x+4) * (y+4))
    soma += sequencia
    n -= 1
    x += 4
    y += 4

print(f'{soma:.4f}')