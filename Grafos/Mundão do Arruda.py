def ler_caminhos(pontos):
    conexoes = []

    for _ in range(len(pontos) - 1):
        entrada = list(map(int, input().split()))
        conexoes.append(entrada)

    return conexoes

class Grafo:
    def __init__(self):
        self.nos = {}

    def set_aresta(self, num, nome):
        if num not in self.nos:
            self.nos[num] = []
        self.nos[num].append(nome)


class BSF:
    def __init__(self, no, conexoes):
        self.no = no
        self.conexoes = conexoes
        self.grafo = Grafo()

        for i, conexos in enumerate(conexoes):
            for c in conexos:
                self.grafo.set_aresta(i, c)

    def get_caminho(self, inicio, fim):
        visitados = []
        fila = [(inicio, [])]

        while fila:
            no, caminho = fila.pop(0)
            if no in visitados:
                continue
            visitados.append(no)

            if no == fim:
                return caminho + [no]

            for vizinho in self.grafo.nos.get(no, []):
                fila.append((vizinho, caminho + [no]))

        return []



lugares = input().split()
origem = lugares[0]
destino = lugares[-1]
caminhos = ler_caminhos(lugares)

navegador = BSF(lugares, caminhos)

indice_inicio = lugares.index(origem)
indice_fim = lugares.index(destino)

rota = navegador.get_caminho(indice_inicio, indice_fim)

if rota:
    print(f"Grafite precisou que passar por {len(rota)} locais ao longo do trajeto",
          " -> ".join([lugares[no] for no in rota]) + ".")
else:
    print("Infelizmente Grafite não pode chegar no Arruda.")
