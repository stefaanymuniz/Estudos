# --- Preços dos Produtos (Constantes) ---
PRECO_CERVEJA = 3.20
PRECO_MACARRAO = 3.73
PRECO_MOLHO = 3.45
PRECO_KG_CEBOLA = 5.40
PRECO_KG_ALHO = 30.00
PRECO_KG_PAO = 20.00

quant_cerveja = int(input())
quant_macarrao = int(input())
quant_molho_tomate = int(input())
peso_g_cebola = float(input()) 
peso_g_alho = float(input())
peso_g_pao = float(input())

# --- Cálculos dos Subtotais --
total_cerveja = quant_cerveja * PRECO_CERVEJA
total_macarrao = quant_macarrao * PRECO_MACARRAO
total_molho = quant_molho_tomate * PRECO_MOLHO

total_cebola = (peso_g_cebola/1000) * PRECO_KG_CEBOLA
total_alho = (peso_g_alho/1000) * PRECO_KG_ALHO
total_pao = (peso_g_pao/1000) * PRECO_KG_PAO

# --- Cálculo Final ---
valor_total = total_cerveja + total_macarrao + total_molho + total_cebola + total_alho + total_pao
valor_cada = valor_total/3

print(f'Valor total da compra: R${valor_total:.2f}')
print(f'Valor por pessoa: R${valor_cada:.2f}')