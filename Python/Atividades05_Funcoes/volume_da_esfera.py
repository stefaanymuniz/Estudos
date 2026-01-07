# "raio" é uma Variável Local, ou seja, só existe dentro da função, assim como o "pi" e o "volume"
def VolumeEsfera(raio): 
    pi = 3.1416
    volume = (4 * pi * raio**3) / 3
    return volume


raio01 = float(input())
raio02 = float(input())
raio03 = float(input())

volume01 = VolumeEsfera(raio01)
volume02 = VolumeEsfera(raio02)
volume03 = VolumeEsfera(raio03)

print(f'{volume01:.2f}')
print(f'{volume02:.2f}')
print(f'{volume03:.2f}')