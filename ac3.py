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