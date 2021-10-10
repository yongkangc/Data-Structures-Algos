# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/submissions/

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return
        p_val = p.val
        q_val = q.val
        
        return self.preorderTraversal(root,p_val,q_val)
    
    def preorderTraversal(self,node,p,q):
        if not node:
            return
        
        # base case
        # if both p and q are less the parent, means we have to go to left
        if p< node.val and q<node.val:
            return self.preorderTraversal(node.left,p,q)
        
       # if both p and q are greater than parent, it means the parent is on the right
        if p > node.val and q > node.val:
        
            return self.preorderTraversal(node.right,p,q)
        
        # the recurring case is when p is more than node, but q is less or equals to node or the other way round. it means the split end is found
        else:
            return node
        
class Solution:
    # dfs iterative
    def lowestCommonAncestor(self, root, p, q):
        while root:
            if max(p.val, q.val) < root.val:
                root = root.left
            elif min(p.val, q.val) > root.val:
                root = root.right
            else:
                return root
        return None
        
    