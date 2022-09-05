nota1 = float(input('Insira nota 1° Bimestre: '))
nota2 = float(input('Insira nota 2° Bimestre: '))
media = (nota1 + nota2)/2

print(f'A média é: {media}')

if media >= 6:
    print(f'Aprovado com média {media}')
elif media >= 3:
    pf = float(input('Digite a nota da Prova Final: '))
    media = (media + pf) / 2
    if media >= 5:
        print(f'Aprovado na recuperação com média {media}')
    else:
        print(f'Reprovado na recuperação com média {media}')
else:
    print(f'Reprovado com média {media}')

