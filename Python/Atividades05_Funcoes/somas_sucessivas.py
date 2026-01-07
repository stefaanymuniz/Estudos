def SomaSucessiva(num1, num2):
    # Caso Base
    if num2 == 0:
        return 0
    # Caso recursivo
    elif num2 > 0:
        return num1 + SomaSucessiva(num1, num2 - 1)
    else:
        return -num1 + SomaSucessiva(num1, num2 + 1)


num1 = int(input())
num2 = int(input())

print(SomaSucessiva(num1, num2))

