

Using deque as it has O(1) time complexity for both append and pop operations, compared to list which has O(n) time complexity for both append and pop operations.

The idea for this question is to use BFS to traverse the tree. 
- In order to keep track the number of nodes per level, we can find the length of the queue before we start popping the children nodes.
- The length of the queue allows us to know the number of nodes per level and the number of children to be popped.

```python
import collections
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque()
        queue.append(root)
        output = []
        
        
        while queue:
            level_nodes = len(queue)
            levels = []
            for i in range(level_nodes):
                node = queue.popleft()
                if node:
                    queue.append(node.left)
                    queue.append(node.right)
                    levels.append(node.val)
            
            if levels:
                output.append(levels)
        
        return output
```