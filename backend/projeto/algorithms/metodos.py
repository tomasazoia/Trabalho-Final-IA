import heapq
from .grafo import grafo, todas_heuristicas  # Importar o grafo e TODAS as heurísticas

class Grafo:
    def __init__(self):
        self.grafo = grafo
        self.heuristicas = todas_heuristicas  # dicionário com todas as heurísticas

    def custo_uniforme(self, inicio, destino):
        visitados = set()
        fila = [(0, inicio, [])]
        nos_explorados = 0

        while fila:
            custo, atual, caminho = heapq.heappop(fila)
            if atual in visitados:
                continue
            caminho = caminho + [atual]
            visitados.add(atual)
            nos_explorados += 1

            if atual == destino:
                return caminho, custo, nos_explorados

            for vizinho, peso in self.grafo[atual].items():
                if vizinho not in visitados:
                    heapq.heappush(fila, (custo + peso, vizinho, caminho))

        return None, float('inf'), nos_explorados

    def aprofundamento_progressivo(self, inicio, destino, limite_max=50):
        def dfs_limite(no, destino, limite, caminho, custo, visitados):
            if limite == 0:
                return None, float('inf'), visitados
            if no == destino:
                return caminho + [no], custo, visitados
            visitados.add(no)
            for vizinho, peso in self.grafo[no].items():
                if vizinho not in caminho:
                    resultado, custo_total, visitados = dfs_limite(
                        vizinho, destino, limite - 1, caminho + [no], custo + peso, visitados
                    )
                    if resultado:
                        return resultado, custo_total, visitados
            return None, float('inf'), visitados

        visitados = set()
        for limite in range(1, limite_max + 1):
            resultado, custo, visitados = dfs_limite(inicio, destino, limite, [], 0, visitados)
            if resultado:
                return resultado, custo, len(visitados)
        return None, float('inf'), len(visitados)

    def procura_sofrega(self, inicio, destino):
        heuristica = self.heuristicas[destino]  # heurística adaptada ao destino
        visitados = set()
        fila = [(heuristica[inicio], 0, inicio, [])]  # (h(n), custo acumulado, nó atual, caminho)
        nos_explorados = 0

        while fila:
            _, custo_acumulado, atual, caminho = heapq.heappop(fila)
            if atual in visitados:
                continue
            caminho = caminho + [atual]
            visitados.add(atual)
            nos_explorados += 1

            if atual == destino:
                return caminho, custo_acumulado, nos_explorados  # Retorna o caminho, custo total e nós explorados

            for vizinho, peso in self.grafo[atual].items():
                if vizinho not in visitados:
                    heapq.heappush(fila, (heuristica[vizinho], custo_acumulado + peso, vizinho, caminho))

        return None, float('inf'), nos_explorados  # Retorna infinito se não encontrar o destino

    def a_estrela(self, inicio, destino):
        heuristica = self.heuristicas[destino]  # heurística adaptada ao destino
        visitados = set()
        fila = [(heuristica[inicio], 0, inicio, [])]  # (f(n), g(n), nó atual, caminho)
        nos_explorados = 0

        while fila:
            f, g, atual, caminho = heapq.heappop(fila)
            if atual in visitados:
                continue
            caminho = caminho + [atual]
            visitados.add(atual)
            nos_explorados += 1

            if atual == destino:
                return caminho, g, nos_explorados

            for vizinho, custo in self.grafo[atual].items():
                if vizinho not in visitados:
                    g_novo = g + custo
                    f_novo = g_novo + heuristica[vizinho]
                    heapq.heappush(fila, (f_novo, g_novo, vizinho, caminho))

        return None, float('inf'), nos_explorados