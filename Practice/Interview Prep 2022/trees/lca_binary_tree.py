# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # The idea is that we want to see if the left or right subtree contains p and q

        # if both subtrees contains p and q, it means that the current node is the node

        # if only one tree contain p and q, it means that the sub tree could contain the node

        # if current node is p or q, we return it as it means that we have found that node

        # what happens if we dont find any of the nodes? we continue traversing down to sub tree. If still not found return none

        if not root:
            return

        # return current node as it is present. This recursively can be in left or right subtree
        # how about the case where
        if root.val == p.val or root.val == q.val:
            return root

        left, right = None, None

        if root.left != None:
            left = self.lowestCommonAncestor(root.left, p, q)

        if root.right != None:
            right = self.lowestCommonAncestor(root.right, p, q)

        # this means that both trees contain p n q
        if left != None and right != None:
            return root

        #  the case that lca is found in sub trees and how to pass the resukt back up

        if left == None:
            return right

        if right == None:
            return left

        # time complexity : O(h) -> O(n) since we have to traverse down the whole tree
        # space complexity : call stack O(h)

       