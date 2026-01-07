# Faça um programa que receba o salário de um funcionário, calcule e exiba o novo salário, sabendo-se que este sofreu um aumento de 25%.

salario = eval(input('Digite o seu salário: '))
Nsalario = 25/100 * salario
print('Com o aumento de 25%, seu novo salário será:', Nsalario + salario)
