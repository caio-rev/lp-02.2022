print('Menu\n [1] - Cadastrar\n [2] - Excluir\n [3] - Pesquisar\n [0] - Sair')
opc = int(input('Escolha uma opção: '))
while opc != 0:
	if opc > 3 or opc < 0:
		print('Opção invalida')
	if opc == 1:
		print('Opção "Cadastrar" selecionada')
	if opc == 2:
		print('Opção "Excluir" selecionada')
	if opc == 3:
		print('Opção "Pesquisar" selecionada')
	if opc == 0:
		print('Sair')
		break