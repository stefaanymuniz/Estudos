'''
Faça programa que recebe um tempo dado em segundos e calcula
quantos dias, horas, minutos e segundos ele representa.
'''

segundos = int(input())

dias = segundos // 86400 # 86400 segundos = um dia
segundos %= 86400 # %= é o operador de atribuição de resto, ou seja, a variável "segundos" recebe o resto da divisão de segundos por 86400

horas = segundos // 3600 # 3600 segundos = uma hora
segundos %= 3600 #recebe o resto da divisão de segundos por 3600

minutos = segundos // 60 # 60 segundos = um minuto
segundos %= 60 #recebe o resto da divisão de segundos por 60

print(dias)
print(horas)
print(minutos)
print(segundos)