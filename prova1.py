'''
PROVA PRÁTICA DE PYTHON
Ao término enviar e-mail conforme modelo:
Para:       preti.joao@ifmt.edu.br
Assunto:    Prova 1 de Laboratório de Programação 2022/2
Mensagem:   Caio Rennan Vieira Gomes
Anexo:      prova1.py
'''

def main():
    '''
    Executa todass as questões
    '''

    #1. Faça um programa que leia o valor de um produto, o percentual
    #   do desconto desejado e imprima o valor do desconto e o valor
    #   do produto subtraindo o desconto. (2,0pt)
    valor = float(input('Digite o valor do produto: '))
	perc = float(input('Insira o percentual do desconto: '))
	print(f'O valor do desconto é R${valor*perc/100}')
	print(f'Valor com descondo: R${valor - valor*perc/100}')

    #2. Faça um programa que leia 3 números e imprima o maior deles. (2,0pt)
    a = float(input('Digite um valor: '))
	b = float(input('Digite um valor: '))
	c = float(input('Digite um valor: '))
            
	if a > b and a > c:
	    print(a)
	if b > a and b > c:    
	    print(b)
	if c > a and c > b:
	    print(c)   

    #3. Faça um programa que permita entrar com o nome, a nota da prova 1 e a nota
    #   da prova 2 de um aluno. O programa deve imprimir o nome, a nota da prova 1,
    #   a nota da prova 2, a média das notas e uma das mensagens: "Aprovado",
    #   "Reprovado" ou "em Prova Final"(a média é 7 para aprovação, menor que 3 para
    #   reprovação e as demais em prova final). (2,0pt)
    nome = input('Insira o nome do aluno: ')
	nota1 = float(input('Digita a primeira nota: '))
	nota2 = float(input('Digita a segunda nota: '))
	media = (nota1+nota2)/2
	print(f'{nome}\n Nota da 1° prova: {nota1}\n Nota da 2° prova: {nota2}\n Média: {media}')
	if media >= 7:
	    print('Aprovado')
	elif media >= 3:
	 	print('Em prova final')
	else:
	 	print('Reprovado')

    #4. Faça um programa que apresente um menu com 4 opções:
    #   [1] - Cadastrar
    #   [2] - Excluir
    #   [3] - Pesquisar
    #   [0] - Sair
    #   O usuário deve escolher uma opção e o programa deve imprimir uma mensagem 
    #   ao entrar em cada opção do menu. O programa só deve encerrar quando a opção
    #   escolhida for zero (0). (2,0pt)
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


    #5. Faça um programa que calcule o retorno de um investimento. (2,0pt)
    #   O programa deve solicitar do usuário o:
    #   - valor que será investido;
    #   - prazo do investimento (meses);
    #   - juros mensal.
	valor = float(input('Valor a ser investido: '))
	prazo = float(input('Tempo de investimento (meses): '))
	jurosm = float(input('Juros mensal: '))
	c = 0
	while c <= prazo:
	invest = valor+(valor*jurosm/100)*prazo
    c += 1
	print(invest)


main()
