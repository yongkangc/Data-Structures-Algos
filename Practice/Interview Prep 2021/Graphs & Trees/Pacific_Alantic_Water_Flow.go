package main

var dirs = [][]int{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}

func pacificAtlantic(heights [][]int) [][]int {
	visitedPaci := make([][]bool, len(heights))
	visitedAla := make([][]bool, len(heights))
	result := [][]int{}

	// populating visit array
	for i := 0; i < len(heights); i++ {
		visitedPaci[i] = make([]bool, len(heights[0]))
		visitedAla[i] = make([]bool, len(heights[0]))
	}

	nrows := len(heights)
	ncolumns := len(heights[0])

	// traverse through both the pacific and the alantic

	// starting dfs traversals from the top left and bottom right
	for rowIndex := 0; rowIndex < len(heights); rowIndex++ {
		// traverse across the rows for pacific
		dfs(heights, rowIndex, 0, &visitedPaci, nrows, ncolumns)

		// traverse across the rows for alantic
		dfs(heights, rowIndex, ncolumns-1, &visitedAla, nrows, ncolumns)

	}

	// starting dfs traversals from the top right and bottom left
	for columnIndex := 0; columnIndex < len(heights[0]); columnIndex++ {
		// traverse across the columns for pacific
		dfs(heights, 0, columnIndex, &visitedPaci, nrows, ncolumns)

		// traverse across the columns for alantic
		dfs(heights, nrows-1, columnIndex, &visitedAla, nrows, ncolumns)
	}

	for rowIndex, _ := range heights {
		for columnIndex, _ := range heights[rowIndex] {
			if visitedPaci[rowIndex][columnIndex] == true && visitedAla[rowIndex][columnIndex] == true {
				result = append(result, []int{rowIndex, columnIndex})

			}
		}
	}
	return result
}

func dfs(heights [][]int, i int, j int, visited *[][]bool, nrows int, ncolumns int) {

	// checking if its out of bound
	if i < 0 || j < 0 || i >= len(heights) || j >= len(heights[0]) || (*visited)[i][j] == true {
		return
	}
	// mark visited as true
	(*visited)[i][j] = true
	// checking if it can flow to adjacent
	for _, d := range dirs {
		x, y := i+d[0], j+d[1] // x and y are the coordinates to move to
		if x < 0 || y < 0 || x >= nrows || y >= ncolumns || heights[x][y] <= heights[i][j] {
			continue
		}
		dfs(heights, i+d[0], j+d[1], visited, nrows, ncolumns)
	}

}
