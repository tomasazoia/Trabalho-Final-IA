import heapq
from .grafo import grafo, heuristica_faro


def custo_uniforme(inicio, objetivo):
    fila = [(0, inicio, [inicio])]  # (custo acumulado, nó atual, caminho percorrido)
    visitados = set()

    while fila:
        custo, atual, caminho = heapq.heappop(fila)

        print(f"Visitando: {atual}, Custo: {custo}, Caminho: {caminho}")

        if atual == objetivo:
            print(f"\n➡️ Caminho final: {caminho}, Distância total: {custo} km\n")
            return caminho, custo

        if atual in visitados:
            continue

        visitados.add(atual)

        for vizinho, distancia in grafo.get(atual, {}).items():
            if vizinho not in visitados:
                heapq.heappush(fila, (custo + distancia, vizinho, caminho + [vizinho]))

    return None, float("inf")


def procura_sofrega(inicio, objetivo="Faro"):
    fila = [(heuristica_faro[inicio], inicio, [inicio])]  # (heurística, nó atual, caminho percorrido)
    visitados = set()

    while fila:
        heur, atual, caminho = heapq.heappop(fila)

        print(f"Visitando: {atual}, Heurística: {heur}, Caminho: {caminho}")

        if atual == objetivo:
            print(f"\n➡️ Caminho final: {caminho}\n")
            return caminho, heur  # Retorna o caminho e a heurística final

        if atual in visitados:
            continue

        visitados.add(atual)

        for vizinho in grafo.get(atual, {}):
            if vizinho not in visitados:
                heapq.heappush(fila, (heuristica_faro[vizinho], vizinho, caminho + [vizinho]))

        distancia_total = sum(
            grafo[caminho[i]][caminho[i+1]] for i in range(len(caminho) - 1)
        )
        return caminho, distancia_total


def a_estrela(inicio, objetivo="Faro"):
    fila = [(heuristica_faro[inicio], 0, inicio, [inicio])]  # (f = g + h, custo acumulado, nó atual, caminho percorrido)
    visitados = set()

    while fila:
        f, custo, atual, caminho = heapq.heappop(fila)

        print(f"Visitando: {atual}, F: {f}, Custo: {custo}, Caminho: {caminho}")

        if atual == objetivo:
            print(f"\n➡️ Caminho final: {caminho}, Distância total: {custo} km\n")
            return caminho, custo

        if atual in visitados:
            continue

        visitados.add(atual)

        for vizinho, distancia in grafo.get(atual, {}).items():
            if vizinho not in visitados:
                novo_custo = custo + distancia
                f = novo_custo + heuristica_faro[vizinho]
                heapq.heappush(fila, (f, novo_custo, vizinho, caminho + [vizinho]))

    return None, float("inf")


def profundidade_limitada(atual, objetivo, limite, caminho, visitados):
    if atual == objetivo:
        return caminho

    if limite <= 0:
        return None

    visitados.add(atual)

    for vizinho in grafo.get(atual, {}):
        if vizinho not in visitados:
            novo_caminho = profundidade_limitada(
                vizinho, objetivo, limite - 1, caminho + [vizinho], visitados
            )
            if novo_caminho:
                return novo_caminho

    return None


def aprofundamento_progressivo(inicio, objetivo):
    limite = 0
    while True:
        visitados = set()
        print(f"\n🔁 Tentando com profundidade {limite}")
        caminho = profundidade_limitada(inicio, objetivo, limite, [inicio], visitados)

        if caminho:
            # Calcula distância real usando os pesos do grafo
            distancia_total = sum(
                grafo[caminho[i]][caminho[i + 1]] for i in range(len(caminho) - 1)
            )
            print(f"\n➡️ Caminho final: {caminho}, Distância total: {distancia_total} km\n")
            return caminho, distancia_total

        limite += 1