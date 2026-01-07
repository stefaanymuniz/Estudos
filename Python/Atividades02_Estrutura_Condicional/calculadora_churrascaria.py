opcao_carne_completo = 'C'
opcao_bovina_frango = 'BF'
opcao_bovina_suino = 'BS'

preco_kg_bovina = 32.00
preco_kg_frango = 18.00
preco_kg_suina = 15.00
preco_cerveja = 8.00
preco_refri = 6.00

kg_bovina_completo_adulto = 0.2
kg_frango_completo_adulto = 0.1
kg_suina_completo_adulto = 0.1
kg_bovina_completo_crianca = 0.2

kg_bovina_bf_adulto = 0.25
kg_frango_bf_adulto = 0.15
kg_bovina_bf_crianca = 0.2

kg_bovina_bs_adulto = 0.25
kg_suina_bs_adulto = 0.15
kg_bovina_bs_crianca = 0.2

quant_cerveja = 2
quant_refri = 0.5
valor_total = 0

opcao_carne = input()
if opcao_carne != opcao_carne_completo and\
   opcao_carne != opcao_bovina_frango and\
   opcao_carne != opcao_bovina_suino:
    print('Opção inválida.')
else:
    pao_alho = input()
    bebida_adulto = input()
    bebida_crianca = input()
    quant_crianca = int(input())
    quant_adulto = int(input())

    if opcao_carne == opcao_carne_completo:
        valor_total += kg_bovina_completo_adulto * quant_adulto * preco_kg_bovina
        valor_total += kg_frango_completo_adulto * quant_adulto * preco_kg_frango
        valor_total += kg_suina_completo_adulto * quant_adulto * preco_kg_suina
        valor_total += kg_bovina_completo_crianca * quant_crianca * preco_kg_bovina

    elif opcao_carne == opcao_bovina_frango:
        valor_total += kg_bovina_bf_adulto * quant_adulto * preco_kg_bovina
        valor_total += kg_frango_bf_adulto * quant_adulto * preco_kg_frango
        valor_total += kg_bovina_bf_crianca * quant_crianca * preco_kg_bovina

    elif opcao_carne == opcao_bovina_suino:
        valor_total += preco_kg_bovina*kg_bovina_bf_adulto * quant_adulto 
        valor_total += preco_kg_suina*kg_suina_bs_adulto * quant_adulto
        valor_total += preco_kg_bovina*kg_bovina_bf_crianca * quant_crianca

    if bebida_adulto == 'S':
        valor_total += quant_cerveja * quant_adulto * preco_cerveja

    if bebida_crianca == 'S':
        valor_total += quant_refri * quant_crianca * preco_refri

    if pao_alho == 'N':
        valor_total = valor_total * 0.98

    print(f'R$: {valor_total:.2f}')