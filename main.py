class Directed_Graph:
    """
    Clase que representa un grafo dirigido.
    Permite agregar nodos, aristas y obtener información sobre la conectividad del grafo.
    """
    def __init__(self):
        self.graph_dict = {}  # Diccionario para almacenar los nodos y sus conexiones
        self.nodes = []  # Lista para almacenar los nombres de los nodos

    def add_node(self, node):
        """
        Agrega un nodo al grafo si no existe previamente.
        
        Parámetros:
        - node: Objeto de tipo Node que representa el nodo a agregar.
        """
        if node in self.graph_dict:
            return "El nodo ya está en el grafo"
        self.graph_dict[node] = []
        self.nodes.append(node.get_name())

    def add_edge(self, edge):
        """
        Agrega una arista dirigida entre dos nodos existentes en el grafo.
        
        Parámetros:
        - edge: Objeto de tipo Edge que representa la arista a agregar.
        """
        n1 = edge.get_n1()
        n2 = edge.get_n2()
        weight = edge.get_weight()
        
        if n1 not in self.graph_dict:
            raise ValueError(f"Nodo {n1.get_name()} no existe")
        if n2 not in self.graph_dict:
            raise ValueError(f"Nodo {n2.get_name()} no existe")
        
        self.graph_dict[n1].append((n2, weight))

    def is_node_in(self, node):
        """
        Verifica si un nodo existe en el grafo.
        
        Parámetros:
        - node: Objeto de tipo Node a verificar.
        
        Retorna:
        - True si el nodo está en el grafo, False en caso contrario.
        """
        return node in self.graph_dict
    
    def get_node(self, node_name):
        """
        Devuelve el nodo con el nombre especificado si existe en el grafo.
        
        Parámetros:
        - node_name: Nombre del nodo a buscar.
        
        Retorna:
        - Objeto de tipo Node si existe, de lo contrario imprime un mensaje de error.
        """
        for n in self.graph_dict:
            if node_name == n.get_name():
                return n
        print(f"El nodo {node_name} no existe")
    
    def get_all_nodes(self):
        """
        Retorna una lista con los nombres de todos los nodos en el grafo.
        """
        return self.nodes
    
    def get_neighbours(self, node):
        """
        Devuelve los nodos vecinos a los que se puede llegar desde el nodo dado.
        
        Parámetros:
        - node: Nodo del cual se buscan los vecinos.
        
        Retorna:
        - Lista de tuplas con los nodos vecinos y el peso de la conexión.
        """
        if node not in self.graph_dict:
            print(f"El nodo {node.get_name()} no se encuentra en el grafo")
            return []
        return self.graph_dict[node]
    
    def get_incoming_neighbours(self, node):
        """
        Devuelve los nodos que tienen una arista dirigida hacia el nodo dado.
        
        Parámetros:
        - node: Nodo para el que se buscan conexiones entrantes.
        
        Retorna:
        - Lista de tuplas con los nodos entrantes y el peso de la conexión.
        """
        if node not in self.graph_dict:
            print(f"El nodo {node.get_name()} no se encuentra en el grafo")
            return []

        incoming_neighbours = []
        for n in self.graph_dict:
            for neighbor, weight in self.graph_dict[n]:
                if neighbor == node:
                    incoming_neighbours.append((n, weight))

        return incoming_neighbours
    
    def __str__(self):
        """
        Devuelve una representación en cadena del grafo, mostrando las aristas y sus pesos.
        """
        all_edges = ""
        for n1 in self.graph_dict:
            for n2, weight in self.graph_dict[n1]:
                all_edges += f"{n1.get_name()} --({weight})--> {n2.get_name()}\n"
        return all_edges

class Edge:
    """
    Representa una arista dirigida con un peso entre dos nodos en el grafo.
    """
    def __init__(self, n1, n2, weight=1):
        self.n1 = n1
        self.n2 = n2
        self.weight = weight

    def get_n1(self):
        return self.n1

    def get_n2(self):
        return self.n2

    def get_weight(self):
        return self.weight

    def __str__(self):
        return f"{self.n1.get_name()} --({self.weight})--> {self.n2.get_name()}"
    
class Node:
    """
    Representa un nodo en el grafo, identificado por un nombre único.
    """
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def __str__(self):
        return self.name
    

def build_custom_graph(graph):
    """
    Crea y devuelve un grafo dirigido con nodos y aristas predefinidos para pruebas.
    
    Parámetros:
    - graph: Clase de grafo que se va a instanciar.
    
    Retorna:
    - Objeto del grafo con los nodos y aristas añadidos.
    """
    g = graph()
    
    # Crear nodos (0-8)
    nodes = {i: Node(str(i)) for i in range(9)}
    for node in nodes.values():
        g.add_node(node)

    # Agregar aristas con pesos
    edges = [
        (0, 1, 2), (0, 2, 4), (0, 4, -2), (0, 5, 1), (0, 6, 5),
        (2, 3, 3), (2, 4, 2), (3, 8, -4), (4, 3, 5), (4, 8, 1),
        (4, 7, 2), (5, 7, -1), (5, 8, -3), (6, 7, 6), (7, 8, 2)
    ]

    for n1, n2, weight in edges:
        g.add_edge(Edge(nodes[n1], nodes[n2], weight))

    return g

def find_paths(graph, source, target, cost=0, path=None):
    """
    Encuentra todos los caminos desde el nodo `source` hasta el nodo `target` en el grafo `graph`.
    
    Parámetros:
    - graph: Objeto del grafo que contiene los nodos y sus conexiones.
    - source: Nodo de inicio.
    - target: Nodo destino.
    - cost: Costo acumulado del camino (por defecto 0).
    - path: Lista de nodos visitados en el camino actual (por defecto None).
    
    Retorna:
    - Lista de tuplas, donde cada tupla contiene un camino (lista de nodos visitados) y su costo.
    """
    if path is None:
        path = []
    path = path + [source.get_name()]

    if source == target:
        return [(path, cost)]

    if not(graph.is_node_in(source)):
        return []

    paths = []
    
    for node, weight in graph.get_neighbours(source):
        if node not in path:
            newpaths = find_paths(graph, node, target, cost + weight, path)
            paths.extend(newpaths)
    
    return sorted(paths, key=lambda x: x[1], reverse=True)


def get_most_reachable(source, graph):
    """
    Encuentra el nodo más alcanzable desde `source`, es decir, el nodo que tiene más caminos posibles desde `source`.
    
    Parámetros:
    - source: Nodo de inicio.
    - graph: Grafo donde se buscan los caminos.
    
    Retorna:
    - Una tupla con el nodo más alcanzable y la cantidad de caminos que lo alcanzan.
    """
    paths = []
    for node in graph.get_all_nodes():
        node_paths = [(node, len(find_paths(graph, source, graph.get_node(node))))]
        paths.extend(node_paths)
    
    return sorted(paths, key=lambda x: x[1], reverse=True)[0]


def set_Vprime(graph, source):
    """
    Inserta un nuevo nodo `V'` en el grafo de manera que tenga más caminos que el nodo más alcanzable original.
    
    Parámetros:
    - graph: Grafo donde se insertará el nodo.
    - source: Nodo de inicio desde donde se mide la alcanzabilidad.
    
    Lanza una excepción si no es posible insertar `V'` de manera que tenga más caminos que el nodo más alcanzable.
    """
    V_name, count_V = get_most_reachable(source, graph)
    V = graph.get_node(f"{V_name}")
  
    vecinos_de_V = set(n.get_name() for n, _ in graph.get_neighbours(V))
    if not vecinos_de_V:
        vecinos_de_V = set(n.get_name() for n, _ in graph.get_incoming_neighbours(V))
    
    Vprima = Node("V'")
    if graph.is_node_in(Vprima):
        print("V' ya está en el grafo")
        return
    
    graph.add_node(Vprima)
    
    nodos_seguro = [
        graph.get_node(n_name) for n_name in graph.get_all_nodes()
        if n_name != V_name and n_name not in vecinos_de_V
    ]
    if not nodos_seguro:
        raise ValueError("❌ No se puede insertar V' porque todos los nodos están conectados a V.")
    
    for nodo in nodos_seguro:
        graph.add_edge(Edge(nodo, Vprima, 1))
    
    paths_to_Vprima = find_paths(graph, source, Vprima)
    count_Vprima = len(paths_to_Vprima)
    
    if count_Vprima > count_V:
        print("✅ V' fue insertado con éxito.")
        print("Número de caminos a V':", count_Vprima)
        for nodo in nodos_seguro:
            print(f"{nodo.get_name()},1,V'")
    else:
        raise ValueError("❌ No fue posible hacer que V' sea más alcanzable que V.")


if __name__ == "__main__":
    """
    Punto de entrada del programa. Construye un grafo de prueba, encuentra el nodo más alcanzable
    y trata de insertar el nodo `V'` para mejorar la alcanzabilidad general.
    """
    G = build_custom_graph(Directed_Graph)
    V, total_paths = get_most_reachable(G.get_node("0"), G)
    paths = find_paths(G, G.get_node("0"), G.get_node(V))

    print(f"El nodo alcanzable por la mayor cantidad de caminos partiendo desde '0' es '{V}' con un total de {total_paths} caminos\n")
    for i, path in enumerate(paths):
        print(f"{i+1} - {path}")

    set_Vprime(G, G.get_node("0"))