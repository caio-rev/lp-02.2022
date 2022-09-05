tempo = float(input('Tempo de viagem (em horas): ')) 
vmedia = float(input('Velocidade média em km/h: '))

print(f'Distancia percorrida: {round(tempo*vmedia, 2)} km')
print(f'Combustível consumido: {round(tempo*vmedia/12, 2)} litros')