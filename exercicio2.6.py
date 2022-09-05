slbruto = float(input("Informe o salário bruto: R$"))
vlprestacao = float(input("Insira o valor da prestação desejada: R$"))
porcentagem = 30 * slbruto/100

if vlprestacao > porcentagem:
    print('O empréstimo não pôde ser concedido pois ultrapassa 30% da sua renda bruta')
else:    
    print('O empréstimo é valido')