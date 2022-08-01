
valorProd = float(input('Qual o valor do produto? '))
tipoCliente = input('Tipo de cliente: ').strip().upper()
valorDesc = 0


if tipoCliente == 'PLATINUM':
    valorDesc = (valorProd*10)/100
elif tipoCliente == 'GOLD':
    valorDesc = (valorProd*7)/100
elif tipoCliente == 'BRONZE':
    valorDesc = (valorProd*4)/100
else:
    valorDesc = 0

print(f'Valor do produto: R$ {valorProd}\n')
print(f'Desconto: R$ {valorDesc} ({tipoCliente})\n')
print(f'Produto com desconto: R$ {valorProd - valorDesc}\n')