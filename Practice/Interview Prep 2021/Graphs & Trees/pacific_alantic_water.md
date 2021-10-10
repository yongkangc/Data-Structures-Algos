One potential improvemnent i could make is to use set to hold the list.
Why set?

Template for DFS Matrix Question

```python
def dfs(matrix):
    # 1. Check for an empty graph.
    if not matrix:
        return []

    # 2. Initialize
    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

    def traverse(i, j):
        # a. Check if visited
        if (i, j) in visited:
            return
  # b. Else add to visted
        visited.add((i, j))

        # c. Traverse neighbors.
        for direction in directions:
            next_i, next_j = i + direction[0], j + direction[1]
            if 0 <= next_i < rows and 0 <= next_j < cols:
                # d. Add in your question-specific checks.
                traverse(next_i, next_j)

    # 3. For each point, traverse it.
    for i in range(rows):
        for j in range(cols):
            traverse(i, j)

```


My answer

```python

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights: return []
        self.pacific_tracker = set()
        self.alantic_tracker = set()
        self.visited = set()
        self.directions = [(0,1),(1,0),(-1,0),(0,-1)]
        
        nrows = len(heights)
        ncolumns = len(heights[0])
        
        # start from column
        for rowIndex in range(nrows):
            # take first and last column
            self.dfs(heights,rowIndex,0,self.pacific_tracker)
            self.dfs(heights,rowIndex,ncolumns-1,self.alantic_tracker)
        
        # start from rows 
        for colIndex in range(ncolumns):
            # take first and last row
            self.dfs(heights,0,colIndex,self.pacific_tracker)
            self.dfs(heights,nrows-1,colIndex,self.alantic_tracker)
        print(self.alantic_tracker)
        print(self.pacific_tracker)

        
        # return intersection between sets
        return list(self.pacific_tracker.intersection(self.alantic_tracker))      
    
    
    def dfs(self,heights,i,j,tracker):
        # if visited we dont have to visit again
        if (i,j) in tracker:
            return
        # mark visited 
        tracker.add((i,j))      
        
        curr_height = heights[i][j]
        # traverse to neighboring if neighboring is more than or equals to current value
        for direction in self.directions:
            x = direction[0] + i
            y = direction[1] + j
            if x >= 0 and y >= 0 and x < len(heights) and y < len(heights[0]):
                if heights[x][y] >= heights[i][j]:
                    self.dfs(heights,x,y,tracker)
        



```
