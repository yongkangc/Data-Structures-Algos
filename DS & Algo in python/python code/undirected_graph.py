import sys


def count_degrees(G):
    degrees = 0
    for _, edges in G.items():
        degrees += len(edges)
    return degrees

# count_edges(G): which counts the number of edges in the graph. An edge is defined as a connection between two vertices. The argument G is a dictionary.
def count_edges(G):
    num_edges = 0
    for _, edges in G.items():
        num_edges += len(edges)
    return num_edges // 2


class Vertex:
    def __init__(self, id=""):
        self.id = id
        self.neighbours = {}

    def add_neighbour(self, nbr_vertex, weight=0):
        self.neighbours[nbr_vertex] = weight

    def get_neighbours(self):
        #  returns all the Vertices connected to the current Vertex as a list.
        # The elements of the output list are of Vertex object instances.
        return list(self.neighbours.keys())

    def get_weight(self, neighbour):
        return self.neighbours.get(neighbour)

    def __eq__(self, other):
        return self.id == other.id

    def __lt__(self, other):
        # return True if self.id < other.id else False
        return self.id < other.id

    def __hash__(self):
        # which calls the hash() function on id and returns it.
        # This allows the object to be a dictionary key.
        return hash(self.id)


class Graph:
    def __init__(self):
        self.vertices = {}

    def _create_vertex(self, id):
        return Vertex(id)

    def add_vertex(self, id):
        vertex = self._create_vertex(id)
        self.vertices[id] = vertex

    def get_vertex(self, id):
        return self.vertices.get(id)

    def add_edge(self, start_v, end_v, weight=0):
        self.vertices[start_v].add_neighbour(end_v, weight)

    def get_neighbours(self, id):
        vertex = self.get_vertex(id)
        if not vertex:
            return None
        return vertex.get_neighbours()

    def __contains__(self, id):
        return id in self.vertices.keys()

    def __iter__(self):
        for k, v in self.vertices.items():
            yield v

    @property
    def num_vertices(self):
        return len(self.vertices)


class VertexSearch(Vertex):
    def __init__(self, id=""):
        super().__init__()
        self.id = id
        self.colour = "white"
        self.d = sys.maxsize
        self.f = sys.maxsize
        self.parent = None


class GraphSearch(Graph):
    def __init__(self):
        super().__init__()
    # BEGIN SOLUTION

    def _create_vertex(self, id):
        return VertexSearch(id)


class UGraphSearch(GraphSearch):
    def add_edge(self, start_v, end_v, weight=0):
        self.vertices[start_v].add_neighbour(end_v, weight)
        self.vertices[end_v].add_neighbour(start_v, weight)


class Search2D:
    def __init__(self, g):
        self.graph = g

    def clear_vertices(self):
        for vertex in self.graph:
            vertex.colour = "white"
            vertex.d = sys.maxsize
            vertex.f = sys.maxsize
            vertex.parent = None

    def __iter__(self):
        return iter([v for v in self.graph])

    def __len__(self):
        return len([v for v in self.graph.vertices])


class Queue:
    def __init__(self):
        self.__items = []

    def enqueue(self, item):
        self.__items.append(item)

    def dequeue(self):
        return self.__items.pop(0) if not self.is_empty else None

    def peek(self):
        return self.__items[0]

    @property
    def is_empty(self):
        return len(self.__items) == 0

    @property
    def size(self):
        return len(self.__items)


class SearchBFS(Search2D):
    def __init__(self, g):
        super().__init__(g)
        # self.graph = g

    def search_from(self, start):
        queue = Queue()

        start_vertex = self.graph.get_vertex(start)
        start_vertex.color = "grey"
        start_vertex.d = 0
        start_vertex.parent = None

        queue.enqueue(start)
        while not queue.is_empty:
            vertex_id = queue.dequeue()

            vertex = self.graph.get_vertex(vertex_id)
            vertext_nbrs = self.graph.get_neighbours(vertex_id)
            for nbr_id in vertext_nbrs:
                nbr = self.graph.get_vertex(nbr_id)
                if nbr.colour == "white":
                    nbr.colour = "grey"
                    nbr.d = vertex.d + 1
                    nbr.parent = vertex
                    queue.enqueue(nbr.id)
            vertex.colour = "black"

    def get_shortest_path(self, start, dest):
        if not self.graph.get_vertex(start) or not self.graph.get_vertex(dest):
            return
        if self.graph.get_vertex(start) == self.graph.get_vertex(dest):
            return [start]
        if self.graph.get_vertex(start).d != 0:
            self.clear_vertices()
            self.search_from(start)

        result = []
        self.get_path(start, dest, result)

        return result

    def get_path(self, start, dest, result):
        start_vert = self.graph.get_vertex(start)
        dest_vert = self.graph.get_vertex(dest)
        if not self.graph.get_vertex(dest).parent and start_vert.id != dest_vert.id:
            result += ["No Path"]
            return

        print(f"start : {start}, dest : {dest}")
        result.insert(0, dest)

        print(f"dest : {dest_vert.id}")

        if start_vert.id == dest_vert.id:
            return True

        self.get_path(start, self.graph.get_vertex(dest).parent.id, result)


class SearchDFS(Search2D):
    def __init__(self, g):
        super().__init__(g)
        self.graph = g
        self.time = 0
        self.discovery_time = 0
        self.finishing_time = 0

    def search(self):
        for vertex in self.graph:
            vertex.colour = "white"
            self.parent = None
        self.time = 0

    def dfs_visit(self, vert_id):
        # which is the recursive method for visiting a vertex in Depth-First-Search algorithm.
        if not vert_id or not self.graph.get(vert_id):
            return
        self.time += 1
        # visit the node
        vertex = self.graph.get(vert_id)
        vertex.colour = "grey"

        # visit neighbours
        vertext_nbrs = self.graph.get_neighbours(vert_id)
        for nbr_id in vertext_nbrs:
            nbr = self.graph.get_vertex(nbr_id)
            if nbr.colour == "white":
                nbr.parent = vertex  # why do we want to set parent as vertex
                self.dfs_visit(nbr_id)

        vertex.colour = "black"


g4 = GraphSearch()
g4.add_vertex("e")
g4.add_vertex("m")
g4.add_vertex("a")
g4.add_vertex("c")
g4.add_vertex("s")
g4.add_edge("e", "m")
g4.add_edge("m", "a")
g4.add_edge("a", "c")
g4.add_edge("c", "s")
gs = SearchDFS(g4)
gs.search()
print(gs.graph)
# assert gs.graph.get_vertex("e").parent == None
# assert gs.graph.get_vertex("m").parent == gs.graph.get_vertex("e")

# assert gs.graph.get_vertex("m").d == 2 and gs.graph.get_vertex("a").f == 8
# assert gs.graph.get_vertex("c").d == 4 and gs.graph.get_vertex("s").f == 6
