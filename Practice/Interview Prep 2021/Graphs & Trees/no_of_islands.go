// Also known as flood fill algorithm

// Using DFS solution
func numIslands(grid [][]byte) int {
	islandCounter := 0

	for i := 0; i < len(grid); i++ {
		for j := 0; j < len(grid[0]); j++ {
			// traverse if the cell has '1'
			if grid[i][j] == '1' {
				dfs(grid, i, j)
				islandCounter++
			}
		}
	}
	return islandCounter
}

func dfs(grid [][]byte, i int, j int) {
	// checking if the grid is out of bound or not connected or visited
	if i < 0 || j < 0 || i >= len(grid) || j >= len(grid[0]) || grid[i][j] != '1' {
		return
	}

	// preorder traversal : current,left,,right
	grid[i][j] = '#' // signifies visited

	// traversing around surrounding 1s
	dfs(grid, i, j-1)
	dfs(grid, i, j+1)
	dfs(grid, i+1, j)
	dfs(grid, i-1, j)

}

// In this question, we would have to find all the connected '1's.
// this can be done with graph traversal algorithm where we take in the adjacent matrix
// upon searching the surrounding `1`s, we add +1 to the counter of the island. We would traverse until there is no ones being connected.
// when we visit the node, we would mark it as visited.
// after the node is visited, we stop traversing and continue with the search

// Time complexity O(N*M)
// Space Complexity O(1)