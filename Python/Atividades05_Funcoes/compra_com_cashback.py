def valor_cashback(categoria_cartao, valor_compra):
    if categoria_cartao == 'gold':
        return valor_compra * 0.01, False 
    elif categoria_cartao == 'platinum':
        return valor_compra * 0.025, False
    elif categoria_cartao == 'infinity':
        return valor_compra * 0.05, True
    
def valor_limite(limite, cashback, infinity):
    if infinity == True:
        return cashback
    else:
        if cashback >= limite:
            return limite   
        else:
            return cashback


categoria_cartao = input().lower()
valor_compra = float(input()) 
limite_atual = float(input())
# Primeiro e segundo retorno da função "valor_cashback"
cashback, infinity = valor_cashback(categoria_cartao, valor_compra)

print(f'{valor_limite(limite_atual, cashback, infinity):.2f}')