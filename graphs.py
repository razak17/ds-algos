class Graph:
    """Representation of a simple graph using an adjacency graph
    """
    # -----------------nested Vertex class ------------------
    class Vertex:
        # lightweight structure
        __slots__ = '_element'

        def __init__(self, x):
            # Do not call constructor immediately, use insert_edge()
            self._element = x
        
        def element(self):
            # element associated with vertex
            return self._element

        def __hash__(self):
            # will allow vertex to be a map/ set with a key
            return hash(id(self))

        def __str__(self):
            return str(self._element)

    # ------------------ nested Edge class -------------
    class Edge:
        # lightweight structure
        __slots__ = '_origin', '_destination', '_element'

        def __init__(self, u, v, x):
            # Do not call constructor immediately, use insert_edge()
            self._origin = u
            self._destination = v
            self._element = x

        def endpoints(self):
            # return (u, v) tuples for vertices u and v
            return (self._origin, self._destination)

        def opposite(self, v):
            # return vertex that is opposite v on this edge
            if not isinstance(v, Graph.Vertex):
                raise TypeError("v  must be a vertex!")
            return self._destination if v is self._origin else self._origin
            raise ValueError("v not incident to edge!")

        def element(self):
            # returns element associated with this edge
            return self._element

        def __hash__(self):
            return hash((self._origin, self._destination))

        def __str__(self):
            return '({0}, {1}, {2})'.format(self._origin, self._destination, self._element)


    # ------------------ graph methods -------------
    def __init__(self, directed=False):
        """ create an empty graph (undirected by default)
        graph can be directed if optional parameter is set to True

        """
        self._outgoing = {}
        # only create second map for directed graph
        self._incoming = {} if directed else self._outgoing

    def _validate_vertex(self, v):
        # verify that v is a vertex on the graph
        if not isinstance(v, self.Vertex):
            raise TypeError("Vertex Expected!")
        if v not in self._outgoing:
            raise ValueError("Vertex does not belong to this graph!")

    def is_directed(self):
        return self._incoming is not self._outgoing # directed maps are distinct

    def vertex_count(self):
        # return the number of vertices in the graph
        return len(self._outgoing)

    def vertices(self):
        # iteration of all vertices of graph
        return self._outgoing.keys()

    def edge_count(self):
        # return number of edges in graph
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        #for undirected graphs, make sure not to double count edges
        return total if self.is_directed() else total // 2

    def edges(self):
        # return a set of all edges in the graph
        result = set()
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())   # add edges to resulting set
        return result

    def get_edge(self, u, v):
        # return the edge from u to v, or None if not adjacent
        self._validate_vertex(u)
        self._validate_vertex(v)
        return self._outgoing[u].get(v) 
    
    def degree(self, v, outgoing=True):
        """return number of outgoing edges incident to vertex, v in graph.

        if graph is directed, optional parameter used to count incoming edges
        """
        self._validate_vertex(v)
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incident_edges(self, v, outgoing=True):
        """return all (outgoing) edges incident to vertex v in the graph

        if graph is directed, optional parameter used to request incoming edges
        
        """
        self._validate_vertex(v)
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge

    def insert_vertex(self, x=None):
        # insert and return a new vertex with element x
        v = self.Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}
        return v

    def insert_edge(self, u, v, x=None):
        # insert and return a new edge from u to v with auxilliary element x
        if self.get_edge(u, v) is not None:
            raise ValueError("u and v are already adjacent")
        e = self.Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e

        
# if __name__ == '__main__':

cc = Graph()
v1 = cc.insert_vertex(2)
v2 = cc.insert_vertex(3)
v3 = cc.insert_vertex(4)
v4 = cc.insert_vertex(5)
v5 = cc.insert_vertex(6)
vertices = cc.vertex_count()

print(vertices)
cc.insert_edge(v1, v2, 9)
print(cc.get_edge(v1, v2))
print(cc.edge_count())
print(cc.is_directed())
cc.insert_edge(v2, v3, 7)
print(cc.edge_count())
cc.insert_edge(v3, v4, 8)
print(cc.incident_edges(9, 7))