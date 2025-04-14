import heapq
from .grafo import grafo, heuristica_faro  # Importar o grafo e as heurísticas do grafo.py

class Grafo:
    def __init__(self):
        # Usar o grafo e heurísticas do grafo.py
        self.grafo = grafo
        self.heuristica = heuristica_faro

    def custo_uniforme(self, inicio, destino):
        visitados = set()
        fila = [(0, inicio, [])]  # (custo acumulado, nó atual, caminho)
        nos_explorados = 0  # Contador de nós explorados

        while fila:
            custo, atual, caminho = heapq.heappop(fila)
            if atual in visitados:
                continue
            caminho = caminho + [atual]
            visitados.add(atual)
            nos_explorados += 1  # Incrementa o contador ao explorar um nó

            if atual == destino:
                return caminho, custo, nos_explorados  # Retorna também os nós explorados

            for vizinho, peso in self.grafo[atual].items():
                if vizinho not in visitados:
                    heapq.heappush(fila, (custo + peso, vizinho, caminho))

        return None, float('inf'), nos_explorados  # Retorna os nós explorados mesmo se não encontrar o destino

    def aprofundamento_progressivo(self, inicio, destino, limite_max=50):
        def dfs_limite(no, destino, limite, caminho, custo, visitados):
            if limite == 0:
                return None, float('inf'), visitados
            if no == destino:
                return caminho + [no], custo, visitados
            visitados.add(no)  # Marca o nó como explorado
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
                return resultado, custo, len(visitados)  # Retorna o número de nós explorados
        return None, float('inf'), len(visitados)

    def procura_sofrega(self, inicio, destino):
        visitados = set()
        fila = [(self.heuristica[inicio], inicio, [])]  # (heurística, nó atual, caminho)
        nos_explorados = 0  # Contador de nós explorados

        while fila:
            _, atual, caminho = heapq.heappop(fila)
            if atual in visitados:
                continue
            caminho = caminho + [atual]
            visitados.add(atual)
            nos_explorados += 1  # Incrementa o contador ao explorar um nó

            if atual == destino:
                return caminho, nos_explorados  # Retorna também os nós explorados

            for vizinho in self.grafo[atual]:
                if vizinho not in visitados:
                    heapq.heappush(fila, (self.heuristica[vizinho], vizinho, caminho))

        return None, nos_explorados  # Retorna os nós explorados mesmo se não encontrar o destino

    def a_estrela(self, inicio, destino):
        visitados = set()
        fila = [(0 + self.heuristica[inicio], 0, inicio, [])]  # (f(n), g(n), nó atual, caminho)
        nos_explorados = 0  # Contador de nós explorados

        while fila:
            f, g, atual, caminho = heapq.heappop(fila)
            if atual in visitados:
                continue
            caminho = caminho + [atual]
            visitados.add(atual)
            nos_explorados += 1  # Incrementa o contador ao explorar um nó

            if atual == destino:
                return caminho, g, nos_explorados  # Retorna também os nós explorados

            for vizinho, peso in self.grafo[atual].items():
                if vizinho not in visitados:
                    g_novo = g + peso
                    f_novo = g_novo + self.heuristica[vizinho]
                    heapq.heappush(fila, (f_novo, g_novo, vizinho, caminho))

        return None, float('inf'), nos_explorados  # Retorna os nós explorados mesmo se não encontrar o destino