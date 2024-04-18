from .Vertice import Vertice
import matplotlib.pyplot as plt
import networkx as nx
import random
import heapq

class Grafo:
    def __init__(self):
        self.adjacencia = {} # LISTA DE ADJACÊNCIA
        self.Vertices = [] # LISTA COM OS VÉRTICES DO GRAFO (OBJETO)
        self.posicoes = {} # POSIÇÕES PARA O PLOT COM O MATPLOTLIB

    # SETTERS
    def setArestas(self,origem,destino):
        """
        Insere uma aresta entre dois vértices no Grafo.

        Entrada:
            - vertice_origem: vértice de onde a aresta parte.
            - vertice_destino: vértice para onde a aresta se dirige.

        Observações:
            - Os vértices devem pertencer ao Grafo em que a aresta será inserida.
            - Esta função não lida com a inserção de vértices.
            - Caso a aresta já exista no Grafo, esta função não terá efeito.
        """
        origemV = self.buscaVertice(origem)
        destinoV = self.buscaVertice(destino)
        if destinoV and origemV:
            self.adjacencia[origem].append(destino)
            self.adjacencia[destino].append(origem)

    def setVertice(self,valor):
        """
        Insere um vértice no Grafo.

        Entrada:
            - valor: O valor ou nome a ser atribuído ao vértice.
        """
        if valor not in self.adjacencia.keys():
            verticeaux = Vertice(valor)
            self.adjacencia[verticeaux.getNome()] = []
            self.Vertices.append(verticeaux)
    
    # GETTERS

    def getVertices(self):
        """
        Retorna a listas de adjacência do Grafo.

        Saída:
            - Lista de adjacência do Grafo.
        """
        if len(self.adjacencia)>=1:
            return list(self.adjacencia)
    def getVertice(self,vert):
        """
        Retorna o objeto do vértice.

        Entrada:
            - (vert): O valor ou nome do vértice cujo objeto será retornado.

        Saída:
            - Objeto que representa o vértice especificado.
        """
        for i in self.Vertices:
            if str(vert) == str(i.getNome()):
                return i
        return None
    def getObjectVertice(self):
        """
        Retorna a lista de objetos de todos os vértices do Grafo.

        Saída:
            - Lista de objetos que representa os vértices do Grafo.

        Observações:
            - Esta função retorna todos os vértices do Grafo como uma lista de objetos.
        """
        return self.Vertices
    
    def removeAresta(self, u,v):
        """
        Remove uma determinada aresta do Grafo.

        Entrada:
            - u: vértice de onde a aresta parte.
            - v: vértice para onde a aresta se dirige.
        """
        if self.buscaVertice(u) and self.buscaVertice(v):
            self.adjacencia[v].remove(u)
            self.adjacencia[u].remove(v)

    def buscaVertice(self,vertice):
        """
        Busca se um determinado Vértice existe no Grafo.

        Saída:
            - True: O vértice está no Grafo
            - False: O vértice não está no grafo
        """
        for i in self.Vertices:
            if vertice == i.getNome():
                return True
                break
        return False
    
    
    def imprimirListaAdj(self):
        """
        Imprime do terminal a lista de Adjacência do Grafo.

        Saída:
            - Print no terminal da lista de adjacência do Grafo.
        """
        for vertice,adjacencia in self.adjacencia.items():
            print(vertice,adjacencia)
            
    def imprimirGrafo(self, vertice_atual):
        """
        Imprime no terminal informações pertinentes ao Grafo

        """
        # Imprimir o vértice atual
        print("Local Atual:", vertice_atual)
        #CAMINHOS
        print("Caminhos:")
        for destino in self.adjacencia.get(vertice_atual, []):
            print(f"{vertice_atual}---{destino}")
        # Imprimir os vértices conectados ao vértice atual
        print("Locais para onde posso seguir:")
        for destino in self.adjacencia.get(vertice_atual, []):
            print(destino)

    def dijkstra(self, start, end):
        """
        Executa o algoritmo de Dijkstra para encontrar o caminho mais curto de um vértice de origem para um vértice de destino em um Grafo.

        Entrada:
            - start: O vértice de origem do qual se deseja encontrar o caminho mais curto.
            - end: O vértice de destino para o qual se deseja encontrar o caminho mais curto.

        Saída:
            - Uma lista representando o caminho mais curto do vértice de origem ao vértice de destino, 
            ou uma lista vazia se não houver caminho possível.

        Observações:
            - Este algoritmo implementa o algoritmo de Dijkstra, que é usado para encontrar o caminho mais 
            curto em um grafo ponderado e direcionado, onde os pesos das arestas são não negativos.
            - A função retorna uma lista contendo os vértices que compõem o caminho mais curto do vértice de 
            origem ao vértice de destino, ou uma lista vazia se não houver caminho possível.
        """
        # Inicializa o dicionário de distâncias, o dicionário de predecessores e o heap
        distances = {vertex.getNome(): float('infinity') for vertex in self.Vertices}
        predecessors = {vertex.getNome(): None for vertex in self.Vertices}
        distances[start] = 0
        heap = [(0, start)]
        
        while heap:
            # Pega o vértice com menor custo
            current_distance, current_vertex = heapq.heappop(heap)
            
            # Se já tivermos uma distância menor para esse vértice, continuamos
            if current_distance > distances[current_vertex]:
                continue
            
            # Para cada vizinho do vértice atual
            for neighbor in self.adjacencia[current_vertex]:
                weight = 1  # Peso de cada aresta é considerado como 1
                
                distance = current_distance + weight
                
                # Se encontrarmos uma distância menor para chegar a este vizinho, atualizamos
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    predecessors[neighbor] = current_vertex
                    heapq.heappush(heap, (distance, neighbor))
        
        # Reconstrói o caminho mínimo
        path = []
        current_vertex = end
        while current_vertex is not None:
            path.insert(0, current_vertex)
            current_vertex = predecessors[current_vertex]
        if path[0] == start:
            return path
        else:
            return []
        
    def plotarGrafo(self,nodeAtual):
        """
        Plota o grafo representado pelos vértices e arestas do Grafo atual.

        Entrada:
            - nodeAtual: O vértice atual onde o personagem se encontra.

        Saída:
            - Gráfico visualizando o Grafo com os vértices e arestas, destacando o 
            vértice atual e atributos específicos dos vértices.
        """
        G = nx.Graph()
        
        # Adicionando vértices
        for vertice in self.adjacencia:
            G.add_node(vertice)
        
        # Adicionando arestas
        for origem, destinos in self.adjacencia.items():
            for destino in destinos:
                G.add_edge(origem, destino)

        if not self.posicoes:  # Se o dicionário de posições estiver vazio, calcule as posições
            self.posicoes = nx.spring_layout(G)
        
        # Definindo cores para os vértices
                
        cores = [
            "blue" if vertice == len(self.Vertices) else  # Cor salmon para o vértice 14
            "magenta" if vertice == 1 else   # Cor magenta para o vértice 1
            "green" if self.getVertice(vertice).getECheckPoint() else
            "gray" if vertice == nodeAtual else
            "skyblue"                        # Cor skyblue para os demais vértices
            for vertice in G.nodes()
        ]



        subrotulos = {vertice: f"Subrótulo {vertice}" for vertice in G.nodes()}  # Subrótulos simples usando o valor do vértice
        
        # Plotando o grafo
        nx.draw(G, self.posicoes, with_labels=False, node_size=700, node_color=cores, font_size=12, font_weight="bold", edge_color="black", linewidths=0,width=3.5, alpha=1)
        # Desenhando os rótulos dos vértices principais com diferentes cores
        nx.draw_networkx_labels(G, self.posicoes, font_size=12, font_weight="bold", font_color="black")  # Altere a cor dos rótulos para azul

        # Desenhando os subrótulos
        subrotulos_y_offset = -0.05  # Define o deslocamento vertical dos subrótulos em relação aos rótulos principais
        for vertice, (x, y) in self.posicoes.items():
            subrotulo = subrotulos.get(vertice, "")
            plt.text(x, y + subrotulos_y_offset, subrotulo, fontsize=10, color='black', ha='center', va='top')

        # Adicione a legenda de cores
        plt.legend(handles=[
            plt.scatter([], [], color='blue', label='TESOURO'),
            plt.scatter([], [], color='magenta', label='PRAIA'),
            plt.scatter([], [], color='green', label='CHECKPOINT'),
            plt.scatter([], [], color='gray', label='POSIÇÃO ATUAL'),
        ], loc='best')

        plt.title("MAPA")
        plt.show()