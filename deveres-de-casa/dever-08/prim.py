import heapq

def prim(grafo, inicio):
    visitados = set([inicio])
    arestas = []
    fila = []

    # adiciona arestas iniciais à fila
    for vizinho, peso in grafo[inicio]:
        heapq.heappush(fila, (peso, inicio, vizinho))

    custo_total = 0

    while fila:
        peso, origem, destino = heapq.heappop(fila)

        if destino not in visitados:
            visitados.add(destino)
            arestas.append((origem, destino, peso))
            custo_total += peso

            # adiciona novas arestas do vértice incluído
            for vizinho, p in grafo[destino]:
                if vizinho not in visitados:
                    heapq.heappush(fila, (p, destino, vizinho))

    return custo_total, arestas


# Grafo
grafo = {
    'A': [('B', 2), ('C', 6), ('D', 3)],
    'B': [('A', 2), ('D', 5)],
    'C': [('A', 6), ('D', 4)],
    'D': [('A', 3), ('B', 5), ('C', 4)]
}

custo, mst = prim(grafo, 'A')

print("Custo total:", custo)
print("Arestas da MST:")

for origem, destino, peso in mst:
    print(f"{origem} -> {destino} (peso {peso})")