import random

lista = []
for vlr in range (10):
	lista.append(chr(random.randrange(65,90)))
	print(f'[{vlr}] = {lista[vlr]}')