# My notes on DS and Algo

# Table of Contents

1. [Graphs](#Graphs)

   1. [Types of trees:](#tts)
   1. [Tree/Graph Traversal Algorithms](#traversal)
   1. [Heap](#heap)
   1. [Trie](#trie)

1. [Graphs](#Graphs)
   1. [Graph Data Structure](#gds)
   1. [Tree/Graph Traversal Algorithms](#traversal)
      1. [Binary Tree Traversal](#btt)
      1. [Depth First Search](#dfs)
      1. [BFS](#bfs)
      1. [Topological Sort](#topological-sort)

## Trees

**Types of trees:** <a name="tts"></a>

- Binary Search Tree (most interview questions are asking about binary search trees)
  - for each node, its left child is less than the node, which is less than its right child.
- Balanced
  - Balanced means the difference between the heights of the left and right subtrees is no more than 1.
  - This ensures O(log n) time for both search and insert.
- Complete
  - A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.
- Full
  - A full binary tree is a binary tree in which every node has either 0 or 2 children.
- Perfect
  - Full & Complete
- Binary Heaps (Min/Max)
  - Complete Binary Search Tree where each node is smaller than its childs.
  - the root is the minimum
- Tries(Prefix Trees)

### Heap

![alt text](./assets/heap.png "Heap")

### [Trie](./Datastructure%20and%20Algo%20in%20Golang/trie.go)

- A trie is a kind of tree data structure that is used to store a dynamic set of strings.
- A trie is a tree where each node represents a prefix (or partial key).
- Booleans are used to indicate if a prefix is a complete key or not.
  ![alt text](./assets/trie.PNG "Trie")

Key Functions:

- `insert`: Inserts a new key into the trie.

```
1. For each character in the word, create a new node as a child of the current node if it does not already exist.
2. Mark the current node as complete if it is a prefix of the word.
```

- `search`: Searches for a key in the trie.

Time Complexity:

- `insert`: O(lg n)
- `search`: O(m) where m is the length of the key.
- Tradoff?

Use case:

- many problems involving lists of words leverage trie as optimisation
- Storing a dictionary of words for quick lockup
- autocomplete

## Graphs

- Representing Graphs : <a name="gds"></a>

  - [Adjacency List](./Datastructure%20and%20Algo%20in%20Golang/adjacency_list.go)

    - Every Vertex stores a list of adjacent vertices.
    - Each index of a list could be used to represent the vertex and the elements represent adjacent vertices.

      ![alt text](./assets/adjacency_list.PNG "functions and pointers")

  - [Adjacency Matrix](./Datastructure%20and%20Algo%20in%20Golang/adjacency_matrix.go)

    - Representing graphs as 2 dimensional matrix.
      - Edge is represented by the value of i,j in matrix.
      - To add a vertex, add a row and column
    - If the graph is weighted, the value of each matrix would be the weights instead of 1s and 0s.
    - If the graph is undirected, it means that there is symmetry about the diagonal of the matrix, because the edges are bi-directional.

    - Comparing Adjacency Matrix and List

      - Matrix requries more space. n^2
      - Adjancy matrix is faster for Edge lookup O(1) vs O(V)
        Time Complexity

        ![alt text](./assets/lmc.PNG "functions and pointers")

### Tree/Graph Traversal Algorithms <a name="traversal"></a>

- Breadth-first search is guaranteed to find a shortest possible path between two vertices in a graph. Depth-first search is not (and usually does not).
- DFS is preferred if we want to visit every node in the graph.
- DFS : Stack ; BFS : Queue

  ![alt text](./assets/bfsdfsio.PNG "functions and pointers")

#### [Binary Tree Traversal](./Datastructure%20and%20Algo%20in%20Golang/tree_traversal.go) <a name="btt"></a>

**In order**

      1. Visit Left Node
      1. Current Node
      1. Right Node

**Pre Order**

      1. Visit Current Node
      1. Visit Left Node
      1. Visit Right Node

**Post Order**

      1. Visit Left
      1. Right
      1. Current

#### [Depth-First Traversal](./Datastructure%20and%20Algo%20in%20Golang/graph_search.go) <a name="dfs"></a>

- DFS is a recursive algorithm that visits every node in a graph, starting from the source node and proceeding along the edges of the graph.
- DFS implements the order traversal just that it has 'visited' mark, so that it does not repeat the visiting.

#### [Breadth-First Traversal](<(./Datastructure%20and%20Algo%20in%20Golang/graph_search.go)>) <a name="bfs"></a>

- BFS is a iterative algorithm that uses a queue to store the nodes that need to be visited.

**Algorithm:**

```
1. Enqueue the source node
2. while the queue is not empty, dequeue a node
3. Visit the node if not visited
4. Enqueue the children of the node
```

[Ref video](https://www.youtube.com/watch?v=QRq6p9s8NVg&ab_channel=GoGATEIIT)

#### DFS VS BFS

![alt text](./assets/3graph1.png "functions and pointers")

### Topological Sort

Topological Sort is a linear ordering of vertices such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering.

![alt text](./assets/topological_sort.png "topological sort")

Degree of a vertex is the number of edges connected to it.

| In degree :                                                                                         | Out degree :                                             |
| --------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| In degree is the number of edges coming into a vertex. In degree is 0 if the vertex is a leaf node. | Out degree is the number of edges going out of a vertex. |

Applications

- Task Scheduling
- Build Systems
- Course Scheduling

Algorithm:

```
1. Create a set of all vertices with no incoming edges
2. While there are vertices in the set
    1. Pick a vertex u
    2. Remove u from the set
    3. For each vertex v such that there is an edge from u to v
        1. Remove edge uv from graph
        2. Add v to the set
```
