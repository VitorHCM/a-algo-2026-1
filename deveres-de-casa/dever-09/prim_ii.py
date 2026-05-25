import heapq

def prim(grafo, inicio):
    visitados = set([inicio])
    fila = []
    rota = []
    custo_total = 0

    # adiciona arestas do nó inicial
    for vizinho, peso in grafo[inicio]:
        heapq.heappush(fila, (peso, inicio, vizinho))

    while fila:
        peso, origem, destino = heapq.heappop(fila)

        # evita ciclos
        if destino not in visitados:
            visitados.add(destino)
            rota.append((origem, destino, peso))
            custo_total += peso

            # adiciona novas conexões possíveis
            for vizinho, p in grafo[destino]:
                if vizinho not in visitados:
                    heapq.heappush(fila, (p, destino, vizinho))

    return rota, custo_total


# Grafo das cidades
grafo = {
    'A': [('B', 4), ('C', 4)],
    'B': [('A', 4), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 5), ('E', 6)],
    'D': [('B', 5), ('C', 5), ('E', 3), ('F', 4)],
    'E': [('C', 6), ('D', 3), ('F', 2)],
    'F': [('D', 4), ('E', 2)]
}

# Executa Prim começando pela cidade A
rota, total = prim(grafo, 'A')

print("Rotas dos cabos instalados:")
for origem, destino, peso in rota:
    print(f"{origem} --> {destino}: {peso} km")

print(f"\nQuantidade total mínima de cabos: {total} km")