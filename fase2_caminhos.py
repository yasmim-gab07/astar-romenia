
# Fase 2 - Funcoes, custo de caminho e valores g, h e f

from mapa import mapa_romenia, heuristica_bucareste


# PASSO 1 e 2 - Custo de uma estrada
def custo_da_estrada(origem, destino):
    """Retorna a distancia entre duas cidades."""
    for vizinho, custo in mapa_romenia[origem]:
        if vizinho == destino:
            return custo
    return None


# PASSO 3 - Custo de um caminho inteiro
def custo_do_caminho(caminho):
    """Soma as distancias de todas as estradas do caminho."""
    total = 0

    for i in range(len(caminho) - 1):
        total += custo_da_estrada(caminho[i], caminho[i + 1])

    return total


# PASSO 4 - Testes dos caminhos
print("Arad -> Sibiu custa", custo_da_estrada('Arad', 'Sibiu'), "km")
print("Arad -> Bucharest custa", custo_da_estrada('Arad', 'Bucharest'),
      "(nao existe estrada direta)")

por_fagaras = ['Arad', 'Sibiu', 'Fagaras', 'Bucharest']

por_pitesti = [
    'Arad', 'Sibiu', 'Rimnicu Vilcea', 'Pitesti', 'Bucharest'
]

print()
print("Caminho por Fagaras:", " -> ".join(por_fagaras))
print("Custo =", custo_do_caminho(por_fagaras), "km")

print("Caminho por Pitesti:", " -> ".join(por_pitesti))
print("Custo =", custo_do_caminho(por_pitesti), "km")


# PASSO 5 - Mostrar g(n), h(n) e f(n)
def mostrar_g_h_f(caminho):
    print(f' {"cidade":<15} {"g(n)":>5} {"h(n)":>5} {"f(n)":>5}')

    for i in range(len(caminho)):
        cidade = caminho[i]
        g = custo_do_caminho(caminho[:i + 1])
        h = heuristica_bucareste[cidade]
        f = g + h

        print(f' {cidade:<15} {g:>5} {h:>5} {f:>5}')


print()
print("Valores ao longo do caminho por Fagaras:")
mostrar_g_h_f(por_fagaras)

print()
print("Valores ao longo do caminho por Pitesti:")
mostrar_g_h_f(por_pitesti)


# DESAFIO 1 - Caminho alternativo
caminho_desafio = [
    'Arad', 'Timisoara', 'Lugoj', 'Mehadia',
    'Drobeta', 'Craiova', 'Pitesti', 'Bucharest'
]

print()
print("DESAFIO 1 - Caminho alternativo:")
print(" -> ".join(caminho_desafio))
print("Custo total:", custo_do_caminho(caminho_desafio), "km")


# DESAFIO 2 - Valores g, h e f do caminho alternativo
print()
print("DESAFIO 2 - Valores g, h e f:")
mostrar_g_h_f(caminho_desafio)
