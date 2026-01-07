base_cedula = 160
altura_cedula = 70

distancia_ponto_inicial = int(input())
distancia_ponto_final = int(input())

area_cedula = base_cedula * altura_cedula # área de um retângulo
area_trapezio = ((distancia_ponto_final + distancia_ponto_inicial) * altura_cedula)/2

# Se um dos pedaços possuir estritamente mais/menos/igual a metade da área da nota original
if area_trapezio > area_cedula/2:
  print('1')
elif area_trapezio < area_cedula/2:
  print('2')
else:
  print('0')