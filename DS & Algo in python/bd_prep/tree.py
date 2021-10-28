# implement a binary tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root):
        self.root = root


def inOrderTraversal(node: Node, res):
    if not node:
        return
    if node.left:
        res.append(node.left)
        inOrderTraversal(node.left)
    inOrderTraversal(node)
    if node.right:
        res.append(node.right)
        inOrderTraversal(node.right)

    return

# a better way to write it


def inOrderTraversalImp(node: Node):
    if not node:
        return

    inOrderTraversal(node.left)
    print(node.data)  # visit the node
    inOrderTraversal(node.right)
