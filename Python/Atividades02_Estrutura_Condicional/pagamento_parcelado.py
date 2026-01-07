preco_avista = float(input())
quant_parcelado = int(input())

if quant_parcelado == 2:
    preco_total = preco_avista + preco_avista * 0.1
    valor_prestacao = preco_total/2
    print(f"Preço total a ser pago é de R${preco_total:.2f}, dividido em {quant_parcelado}x de R${valor_prestacao:.2f}")
elif quant_parcelado == 3:
    preco_total = preco_avista + preco_avista * 0.15
    valor_prestacao = preco_total/3
    print(f"Preço total a ser pago é de R${preco_total:.2f}, dividido em {quant_parcelado}x de R${valor_prestacao:.2f}")
elif quant_parcelado == 4:
    preco_total = preco_avista + preco_avista * 0.2
    valor_prestacao = preco_total/4
    print(f"Preço total a ser pago é de R${preco_total:.2f}, dividido em {quant_parcelado}x de R${valor_prestacao:.2f}")
elif quant_parcelado == 5:
    preco_total = preco_avista + preco_avista * 0.25
    valor_prestacao = preco_total/5
    print(f"Preço total a ser pago é de R${preco_total:.2f}, dividido em {quant_parcelado}x de R${valor_prestacao:.2f}")
else:
    print("Opção Inválida")