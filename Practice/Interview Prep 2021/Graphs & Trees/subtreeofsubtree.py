# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        
        
        return self.preorderTraversal(root,subRoot)
        
    
    def preorderTraversal(self,node : TreeNode, subNode : TreeNode):
        if not node:
            return False
            
        if node.val == subNode.val and self.compareTree(node,subNode):
            return True
                        
        return self.preorderTraversal(node.left,subNode) or self.preorderTraversal(node.right,subNode)

    def compareTree(self,node,subNode):
        if not node and not subNode:
            return True
        if not node or not subNode:
            return False
        
        if node.val != subNode.val:
            return False
        
        return self.compareTree(node.left,subNode.left) and self.compareTree(node.right,subNode.right)
            
        