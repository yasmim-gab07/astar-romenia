
from mapa import mapa_romenia, heuristica_bucareste

# 1. Mostrar todas as cidades do mapa
print("CIDADES DA ROMENIA:")
for cidade in mapa_romenia:
    print(cidade)

# 2. Mostrar cidades que possuem exatamente uma estrada
print("\nCIDADES COM EXATAMENTE UMA ESTRADA:")
for cidade, conexoes in mapa_romenia.items():
    if len(conexoes) == 1:
        print(cidade)

# 3. Mostrar cidades com heurística menor que 200 km
print("\nCIDADES COM HEURISTICA MENOR QUE 200 KM:")
for cidade, distancia in heuristica_bucareste.items():
    if distancia < 200:
        print(cidade, "-", distancia, "km")

# 4. Encontrar a estrada mais longa
maior_distancia = 0
maior_estrada = ""

for cidade, conexoes in mapa_romenia.items():
    for vizinha, distancia in conexoes.items():
        if distancia > maior_distancia:
            maior_distancia = distancia
            maior_estrada = cidade + " - " + vizinha

print("\nESTRADA MAIS LONGA:")
print(maior_estrada, "-", maior_distancia, "km")
