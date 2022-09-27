valor = float(input('Valor a ser investido: '))
prazo = float(input('Tempo de investimento (meses): '))
jurosm = float(input('Juros mensal: '))
c = 0
while c <= prazo:
    invest = valor+(valor*jurosm/100)*prazo
    c += 1
print(invest)