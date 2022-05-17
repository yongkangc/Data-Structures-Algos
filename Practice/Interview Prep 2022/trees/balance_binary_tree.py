# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None, score=0):
        self.val = val
        self.left = left
        self.right = right
        self.score = score


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # logic
        # for this question, we can simulate the avl tree where we recursively traverse
        # if we hit the leaf node, meaning both left and right are None, we return +1 to the leaf counter
        # if there is a left or right then we

        # so in essence, it is a post order search where we visit the node the last.
        # When we visit the node, we want to check if the left and right have the same score

        return self.postOrderTraversal(root) != -1

    def postOrderTraversal(self, root):
        if not root:
            return 0
        left = self.postOrderTraversal(root.left)
        right = self.postOrderTraversal(root.right)

        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        else:
            return 1 + max(left, right)