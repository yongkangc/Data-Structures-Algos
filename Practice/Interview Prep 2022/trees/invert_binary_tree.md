``` python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # the idea is that we go do a pre order traversal and swap the children if children are present
        # base case is when the node does not have any children
        # pre order : root,left,right
        
        
        def dfs(node):
            if node == None:
                return
            swap(node)
            dfs(node.left)
            dfs(node.right)
        
        def swap(node):
            if node.left == None and node.right == None:
                return
            
            node.right, node.left = node.left, node.right
            
        dfs(root)
        
        return root
```