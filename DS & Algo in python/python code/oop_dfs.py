import sys


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

    def __str__(self):
        # print(f"nbr : {self.get_neighbours()}")
        neighbour_id = [nbr.id for nbr in self.get_neighbours()]
        nbr_string = ", ".join(neighbour_id)

        return f"Vertex {self.id} is connected to: {nbr_string}"


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


g4 = GraphSearch()
g4.add_vertex("A")
g4.add_vertex("B")
g4.add_vertex("C")
g4.add_vertex("D")
g4.add_vertex("E")
g4.add_vertex("F")
g4.add_edge("A", "B")
g4.add_edge("A", "C")
g4.add_edge("B", "C")
g4.add_edge("B", "D")
g4.add_edge("C", "D")
g4.add_edge("D", "C")
g4.add_edge("E", "F")
g4.add_edge("F", "C")
gs4 = SearchBFS(g4)

gs4.search_from("A")
print(gs4.graph.get_vertex("A").d)
print(gs4.graph.get_vertex("B").parent.id)
print(gs4.graph.get_vertex("A").id)

assert gs4.graph.get_vertex("A").d == 0
assert gs4.graph.get_vertex("A").colour == "black"
assert gs4.graph.get_vertex("A").parent == None
assert gs4.graph.get_vertex("B").d == 1
assert gs4.graph.get_vertex("B").colour == "black"
assert gs4.graph.get_vertex("B").parent == gs4.graph.get_vertex("A")
assert gs4.graph.get_vertex("C").d == 1
assert gs4.graph.get_vertex("C").colour == "black"
assert gs4.graph.get_vertex("C").parent == gs4.graph.get_vertex("A")
assert gs4.graph.get_vertex("D").d == 2
assert gs4.graph.get_vertex("D").colour == "black"
gs4.graph.get_vertex("D").parent
assert gs4.graph.get_vertex("D").parent == gs4.graph.get_vertex("B")
ans = gs4.get_shortest_path("A", "D")
print(ans)
assert ans == ["A", "B", "D"]

ans = gs4.get_shortest_path("D", "A")
print(ans)

assert ans == ["No Path"]
ans = gs4.get_shortest_path("E", "D")
print(ans)

assert ans == ["E", "F", "C", "D"]
