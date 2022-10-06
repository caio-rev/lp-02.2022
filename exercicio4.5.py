alunos = []
qtd_alunos = 15
for cont in range(qtd_alunos):
	aluno = {}
	aluno['nome'] = input('Nome: ')
	aluno['nota1'] = round(float(input(f'Entre a 1° nota do(a) estudante: ')), 1)
	aluno['nota2'] = round(float(input(f'Entre a 2° nota do(a) estudante: ')), 1)
	aluno['media'] = round((aluno['nota1']+aluno['nota2'])/2, 1)
	aluno['situacao'] = 'Aprovado' if aluno['media'] >= 6 else 'Reprovado'
	alunos.append(aluno)
for aluno in alunos:
    print(f"{aluno['nome']}\t{aluno['nota1']}\t{aluno['nota2']}\t{aluno['media']}\t{aluno['situacao']}")