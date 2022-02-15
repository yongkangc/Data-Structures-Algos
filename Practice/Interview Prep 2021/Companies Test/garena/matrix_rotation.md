We can iterate over each group of four cells and rotate them.
The cells move in groups when we rotate the image

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])
        for i in range(n // 2 + n % 2): # row 
            for j in range(n // 2): # col
                tmp = matrix[n - 1 - j][i] # store the right most number
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp

```