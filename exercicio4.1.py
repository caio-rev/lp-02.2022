import random

lista =[]
for vlr in range (15):
	lista.append(random.randrange(1,50))
print(lista)
numusuario = int(input('Digite um valor inteiro para ser encontrado: '))
try:
    posicao = lista.index(numusuario)
except:
    posicao = -1
if numusuario >= 0:
    print(f'Valor {numusuario} encontrado na posição {posicao}')
else:
    print('Número {numusuario} não encontrado')