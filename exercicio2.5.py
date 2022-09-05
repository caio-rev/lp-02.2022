print("Descubra se é ou não divisível por 3 e 7")
num = int(input('Digite um número: '))
print(num)
if num % 3 == 0 and	num % 7 == 0:
	print('É divisível por 3 e 7')
else:
    print('Não é divisível')