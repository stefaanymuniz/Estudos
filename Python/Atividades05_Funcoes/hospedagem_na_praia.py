def CalculaHospedagem(tipo_ap, diarias):
    valor_individual = diarias * 125.00
    valor_suite_dupla = diarias * 140.00
    valor_suite_tripla = diarias * 180.00

    if diarias < 3 and tipo_ap == 'individual':
        return valor_individual
    elif diarias < 3 and tipo_ap == 'suíte dupla':
        return valor_suite_dupla
    elif diarias < 3 and tipo_ap == 'suíte tripla':
        return valor_suite_tripla
    else:
        if tipo_ap == 'individual':
            valor_desconto_individual = valor_individual * 0.15
            valor_total_individual = valor_individual - valor_desconto_individual
            return valor_total_individual

        elif tipo_ap == 'suíte dupla':
            valor_desconto_suite_dupla = valor_suite_dupla * 0.15
            valor_total_suite_dupla = valor_suite_dupla - valor_desconto_suite_dupla
            return valor_total_suite_dupla

        elif tipo_ap == 'suíte tripla':
            valor_desconto_suite_tripla = valor_suite_tripla * 0.15
            valor_total_suite_tripla = valor_suite_tripla - valor_desconto_suite_tripla
            return valor_total_suite_tripla
        


tipo_apartamento = input().lower()
quant_diarias = int(input())

print(f'{CalculaHospedagem(tipo_apartamento, quant_diarias):.2f}')