package main

// create a breath first search algorithm
func BFS(graph [][]int, start int) []int {
	// create a queue to store the path
	queue := make([]int, 0)

	// mark the start node as visited
	visited := make([]bool, len(graph))

	// push the start node into the queue
	queue = append(queue, start)

	// mark the start node as visited
	visited[start] = true

	// create a array to store the path
	path := make([]int, len(graph))

	// while the queue is not empty
	for _, v := range queue {
		// visit the adjacent node
		for _, w := range graph[v] {
			// if the adjacent node is not visited
			if !visited[w] {
				// mark the adjacent node as visited
				visited[w] = true
				// add the adjacent node to the queue
				queue = append(queue, w)
				// add the adjacent node to the path
				path[w] = v
			}
		}
	}

	return path
}
