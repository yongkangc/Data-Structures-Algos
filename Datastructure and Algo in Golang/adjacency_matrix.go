// implement a graph using adjacency matrix
package main

import "strconv"

// AdjacencyMatrix is a graph using adjacency matrix
type AdjacencyMatrix struct {
	matrix [][]int
}

// Vertice struct
type Vertice struct {
	name  string
	edges []*Vertice
}

// Add Vertice
func (v *Vertice) Add(v2 *Vertice) {
	v.edges = append(v.edges, v2)
}

// Add Edge
func (g *AdjacencyMatrix) AddEdge(v1, v2 int) {

	g.matrix[v1][v2] = 1
	g.matrix[v2][v1] = 1
}

// Get Vertice
func (g *AdjacencyMatrix) GetVertice(v int) *Vertice {
	return &Vertice{name: strconv.Itoa(v), edges: make([]*Vertice, 0)}
}

// Print Graph
func (g *AdjacencyMatrix) Print() {
	for i := 0; i < len(g.matrix); i++ {
		for j := 0; j < len(g.matrix); j++ {
			if g.matrix[i][j] == 1 {
				println(i, "->", j)
			}
		}
	}
}

// Main
func main() {
	g := &AdjacencyMatrix{
		matrix: [][]int{
			{0, 1, 0, 1, 0},
			{1, 0, 1, 0, 1},
			{0, 1, 0, 0, 1},
			{1, 0, 0, 1, 0},
			{0, 1, 1, 0, 0},
		},
	}

	v1 := g.GetVertice(1)
	v2 := g.GetVertice(2)
	v3 := g.GetVertice(3)
	v4 := g.GetVertice(4)
	v5 := g.GetVertice(5)

	v1.Add(v2)
	v1.Add(v3)
	v1.Add(v4)
	v1.Add(v5)

	g.AddEdge(1, 2)
	g.AddEdge(1, 3)
	g.AddEdge(1, 4)
	g.AddEdge(1, 5)

	g.Print()
}
