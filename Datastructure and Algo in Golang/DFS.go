package main

// create a depth first search algorithm with adjacent matrix
func depthFirstSearch(matrix [][]int, start, end int) bool {
	if start == end {
		return true
	}

	for i := 0; i < len(matrix); i++ {
		for j := 0; j < len(matrix[i]); j++ {
			if matrix[i][j] == 1 {
				matrix[i][j] = 0
				if depthFirstSearch(matrix, start, end) {
					return true
				}
				matrix[i][j] = 1 // mark as visited
			}
		}
	}
	return false
}