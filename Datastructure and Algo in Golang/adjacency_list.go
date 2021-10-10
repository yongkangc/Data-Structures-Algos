package main

import (
	"fmt"
)

// Implements a graph using adjacency list
type Graph struct {
	// A map of all nodes in the graph
	nodes map[int]*Node
	// Number of nodes in the graph
	size int
}

// Vertex Structure
type Node struct {
	// Vertex ID
	id int
	// Neighbors of the node
	neighbors []int
}

// Add Vertex
func (g *Graph) AddVertex(id int) {
	g.nodes[id] = &Node{id: id}
	g.size++
}

// Add Edge
func (g *Graph) AddEdge(from, to int) {
	g.nodes[from].neighbors = append(g.nodes[from].neighbors, to)
	g.nodes[to].neighbors = append(g.nodes[to].neighbors, from)
}

// Get Vertex
func (g *Graph) GetVertex(id int) *Node {
	return g.nodes[id]
}

// Print out the adjaency list
func (g *Graph) print() {
	for _, v := range g.nodes {
		fmt.Println(v.id, ":", v.neighbors)
	}
}

func main() {
	// Print out the adjacency list
	g := &Graph{nodes: make(map[int]*Node), size: 0}
	g.AddVertex(0)
	g.AddVertex(1)
	g.AddVertex(2)
	g.AddVertex(3)
	g.AddVertex(4)
	g.AddVertex(5)
	g.AddEdge(0, 1)
	g.AddEdge(0, 2)
	g.AddEdge(1, 2)
	g.AddEdge(1, 3)
	g.AddEdge(2, 4)
	g.AddEdge(3, 4)
	g.AddEdge(3, 5)
	g.AddEdge(4, 5)
	g.print()
}
