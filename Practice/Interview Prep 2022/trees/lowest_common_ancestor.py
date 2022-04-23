# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # base case to check if 
        low = min(p.val, q.val)
        high = max(p.val, q.val)
        
        # go right if the lowest is still bigger than root 
        if low > root.val and root.right != None: 
            return self.lowestCommonAncestor(root.right,p,q)
        
        # go left if the highest is still smaller than root 
        if high < root.val and root.left != None:
            return self.lowestCommonAncestor(root.left, p, q)
        
        # else we are in the correct subtree. found the split point
        else:
            return root