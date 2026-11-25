
# -*- coding: utf-8 -*-
# Fase 3: No de busca e fronteira

from mapa import mapa_romenia, heuristica_bucareste

# Criando o no inicial
inicio = 'Arad'
g = 0
h = heuristica_bucareste[inicio]

no_inicial = (g + h, g, inicio, [inicio])
fronteira = [no_inicial]

print('Fronteira no começo:', fronteira)

# Retirando o primeiro no
no = fronteira.pop(0)
f_atual, g_atual, cidade_atual, caminho = no

print('\nNo retirado:', no)
print('Fronteira agora:', fronteira)

# Expandindo os vizinhos de Arad
for vizinho, custo_estrada in mapa_romenia[cidade_atual].items():
    novo_g = g_atual + custo_estrada
    novo_h = heuristica_bucareste[vizinho]
    novo_f = novo_g + novo_h
    novo_caminho = caminho + [vizinho]

    fronteira.append((novo_f, novo_g, vizinho, novo_caminho))

print('\nFronteira depois de expandir Arad:')
for item in fronteira:
    print(item)

# Ordenando a fronteira pelo valor f
fronteira.sort(key=lambda no: no[0])

print('\nFronteira ordenada pelo f:')
for item in fronteira:
    print(item)

proximo = fronteira.pop(0)
print('\nProximo no a expandir:', proximo[2], 'com f =', proximo[0])

# DESAFIO 1: expandir Sibiu manualmente
for vizinho, custo_estrada in mapa_romenia['Sibiu'].items():
    novo_g = proximo[1] + custo_estrada
    novo_h = heuristica_bucareste[vizinho]
    novo_f = novo_g + novo_h
    novo_caminho = proximo[3] + [vizinho]

    fronteira.append((novo_f, novo_g, vizinho, novo_caminho))

fronteira.sort(key=lambda no: no[0])

print('\nDesafio 1 - Fronteira depois de expandir Sibiu:')
for item in fronteira:
    print(item)

# DESAFIO 2: ordenar pelo custo g em vez de f
fronteira.sort(key=lambda no: no[1])

print('\nDesafio 2 - Fronteira ordenada pelo custo g:')
for item in fronteira:
    print(item)

print('\nPrimeiro no usando g:', fronteira[0][2])
