package main

import "fmt"

type Node struct {
	val     int
	visited bool
	left    *Node
	right   *Node
}

// DFS implements inorder
func depthFirstSearch(node *Node) {
	if node == nil {
		return
	}
	depthFirstSearch(node.left)
	fmt.Println(node.val)
	// once visited, mark node as true
	node.visited = true
	depthFirstSearch(node.right)

}

// BFS
func breadthFirstSearch(node *Node) {
	if node == nil {
		return
	}
	var queue []*Node
	// enqueue root
	queue = append(queue, node)
	for _, n := range queue {
		if n.visited {
			continue
		}
		fmt.Println(n.val)
		n.visited = true
		// enqueue left and right of the root node
		// the graph will traverse the left and right child before going to child's child
		queue = append(queue, n.left)
		queue = append(queue, n.right)
	}
}

// ref : https://www.youtube.com/watch?v=QRq6p9s8NVg&ab_channel=GoGATEIIT
