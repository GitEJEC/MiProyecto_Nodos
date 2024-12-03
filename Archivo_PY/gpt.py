# Definimos una clase para "grafos dirigidos"
class Directed_Graph:
    def __init__(self):
        # Creamos un grafo "Vacío"
        self.graph_dict = {}
        
    def add_vertex(self, vertex):
        # Medida de seguridad para no añadir dos veces el mismo vértice
        if vertex in self.graph_dict:
            return "Vertex already in graph"
        # Le añadimos al grafo vacío un vértice que contendrá una lista
        self.graph_dict[vertex] = []
        
    def add_edge(self, edge):
        v1 = edge.get_v1()
        v2 = edge.get_v2()
        if v1 not in self.graph_dict:
            raise ValueError(f'Vertex {v1.get_name()} not in graph')
        if v2 not in self.graph_dict:
            raise ValueError(f'Vertex {v2.get_name()} not in graph')
        self.graph_dict[v1].append(v2)
    
    def is_vertex_in(self, vertex):
        # Vemos si es que el vértice ya está añadido en el diccionario
        # Regresa True o False
        return vertex in self.graph_dict
    
    def get_vertex(self, vertex_name):
        # Busca el nombre de un vértice y revisa todos los vértices comparando
        for v in self.graph_dict:
            if vertex_name == v.get_name(): 
                return v
        # Si no encuentra, devuelve que no existe
        print(f'Vertex {vertex_name} does not exist')
    
    def get_neighbours(self, vertex): 
        return self.graph_dict[vertex]
    
    def __str__(self):
        # Vamos a guardar todas las aristas
        all_edges = ''
        for v1 in self.graph_dict:
            for v2 in self.graph_dict[v1]:
                # Va por cada v1 (mostrándolo) señalando sus v2 (destino)
                all_edges += v1.get_name() + ' ---> ' + v2.get_name() + '\n'
        return all_edges

# Creamos una clase de grafo no dirigido
class Undirected_graph(Directed_Graph):
    def add_edge(self, edge):
        super().add_edge(edge)
        # Agregamos el nodo de regreso
        edge_back = Edge(edge.get_v2(), edge.get_v1())
        # Y lo invertimos
        super().add_edge(edge_back)

# Definimos un objeto de tipo Edge
class Edge:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2 
        
    def get_v1(self):
        return self.v1
    
    def get_v2(self):
        return self.v2
    
    def __str__(self):
        return self.v1.get_name() + ' ---> ' + self.v2.get_name()
    
# Definimos un objeto de tipo vertex
class Vertex:
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    def __str__(self):
        return self.name

def build_graph(graph_type):
    g = graph_type()
    # Añadimos los nodos
    for v in ('s', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'x'):
        g.add_vertex(Vertex(v))
    
    # Añadimos las aristas
    edges = [
        ('s', 'a'), ('s', 'b'), ('a', 'c'), ('b', 'd'),
        ('c', 'e'), ('d', 'f'), ('e', 'g'), ('f', 'h'),
        ('g', 'i'), ('h', 'x')
    ]
    
    for v1, v2 in edges:
        g.add_edge(Edge(g.get_vertex(v1), g.get_vertex(v2)))
    
    return g 

# Crear un grafo dirigido
G1 = build_graph(Directed_Graph)

# Imprimir el grafo
print(G1)