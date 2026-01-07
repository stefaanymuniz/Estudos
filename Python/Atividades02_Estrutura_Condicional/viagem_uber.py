# Exercício " A viagem" do The Huxley

salario = float(input("Digite o seu salário: "))
valor_fixo_tarifa = float(input('Valor fixo da tarifa: '))
preco_km = float(input('Preço por km: '))
quilometragem = float(input('Quilometragem rodada: '))
viagem_fds = int(input('Vai viajar esse fim de semana? '))

tarifa = valor_fixo_tarifa + preco_km * quilometragem
salario_viagem = salario * 0.3

if viagem_fds == 1:
    tarifa = tarifa + tarifa * 0.1

if salario_viagem < tarifa:
    print('Não vai poder viajar.')
    print(f'{tarifa - salario_viagem:.2f}')
else:
    print('Vai poder viajar.')
    print(f'{tarifa:.2f}')
    print(f'{salario_viagem - tarifa:.2f}')