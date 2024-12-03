#Forma de Diccionario, funciona pero es mas profesional hacerla con objetos 
#G = {'S': ['A', 'B', 'C', 'D'] }

#crearemos una clase de "grafos dirigidos", para luego crear otra de "no dirigidos"
#que herede de "grafos dirigidos", agregandole el "Camino de vuelta"

#!!!Esto no contempla que los edges tengan valores!!!
class Directed_Graph:
    def __init__(self):
        #Creamos un grafo "Vacio"
        self.graph_dict = {}
    def add_vertex(self, vertex):
        #Medida de seguridad para no añadir dos veces el mismo grafo
        if vertex in self.graph_dict:
            return "Vertex already in graph"
        #Le añadimos al grafo vacio un vertice que contendra una lista
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
        #vemos si es que el vertice ya esta añadido en el diccionario
        #regresa True o False
        return vertex in self.graph_dict
    def get_vertex(self, vertex_name):
        #busca el nombre de un vertice y revisa todos los vertices comparando
        for v in self.graph_dict:
            if vertex_name == v.get_name(): 
                return v
        #si no encuentra revuelve que no existe
        print(f'Vertex {vertex_name} does not exist')
    
    def get_neighbours(self, vertex): 
        return self.graph_dict[vertex]
    
    def __str__(self):
        #vamos a guardar todas las aristas
        all_edges = ''
        for v1 in self.graph_dict:
            for v2 in self.graph_dict[v1]:
                #va por cada v1 (mostrandolo) señalando sus v2 (destino)
                all_edges += v1.get_name() + ' ---> ' + v2.get_name() + '\n'
        return all_edges

#creamos una clase de grafo no dirigido
class Undirected_Graph(Directed_Graph):
    def add_edge(self, edge):
        Directed_Graph.add_edge(self, edge)
        #agregamos el nodo de regreso
        edge_back = Edge(edge.get_v2(), edge.get_v1())
        #y lo invertimos
        Directed_Graph.add_edge(self, edge_back)

#Definimos un objeto de tipo Edge
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
    
#Definimos un objeto de tipo vertex
class Vertex:
    #Los vertices no necesitan nada mas que un nombre
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def __str__(self):
        return self.name

def build_graph(graph):
    g = graph()
   
    # Añadimos los vertices, para esto creare un grafo propio en un posit 
    for v in ('s', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'x'):
    #en vez de añadir edges de uno en uno, haré una variable que contenga una lista con todos los edges
        g.add_vertex(Vertex(v))
    edges = [
        ('s', 'a'), ('s', 'b'), ('s', 'c'), ('a', 'd'),
        ('a', 'i'), ('d', 'h'), ('b', 'e'), ('e', 'x'),
        ('c', 'f'), ('f', 'i') ,('c', 'x'), ('c', 'g')
    ]
    #ahora por cada vertice que haya en edges creara el edge correspondiente
    for v1 , v2 in edges:
        #AñadeVertice (en esta posicion añade v1 , en esta posicion añade v2)
        g.add_edge(Edge(g.get_vertex(v1), g.get_vertex(v2)))
    
    return g 

G1 = build_graph(Directed_Graph)
G2 = build_graph(Undirected_Graph)
print('Grafo dirigido')
print( G1)
print('----------------------------------------')
print('Grafo no dirigido')
print(G2)