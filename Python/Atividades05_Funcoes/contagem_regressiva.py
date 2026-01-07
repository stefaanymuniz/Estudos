def contagem_progressiva(n):
    for num_linha in range(n, 0, -1):
        for contador in range(num_linha):
            
            if contador < num_linha - 1:
                print(num_linha, end = '-')
            else:
                print(num_linha)
        

num = int(input())
contagem_progressiva(num)