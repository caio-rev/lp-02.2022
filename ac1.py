valor = float(input('Digite o valor do produto: '))
perc = float(input('Insira o percentual do desconto: '))
print(f'O valor do desconto é R${valor*perc/100}')
print(f'Valor com descondo: R${valor - valor*perc/100}')