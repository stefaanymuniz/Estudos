'''
Durante a impressão de um conjunto de páginas, o software da impressora mostrou a mensagem: 

“Imprimindo…
75 páginas impressas (12,5% completo) “

Doyoon não lembrava mais quantas páginas tinha o documento dele e, portanto, quantas ainda 
faltavam ser impressas e gostaria de um programa que respondesse isso para ele. Desenvolva 
uma solução para resolver o problema de Doyoon. 
'''

pag_impressas = int(input())
percentual_impressas = float(input())

total_pag = (100 * pag_impressas) / percentual_impressas
pag_restantes = total_pag - pag_impressas

print('O documento possui', round(total_pag),'paginas')
print('Já foram impressas', pag_impressas,'paginas')
print('Faltam', round(pag_restantes),'paginas')
