# Max Depth

Question
Max depth of a binary tree is the longest root-to-leaf path. Given a binary tree, find its max depth.

```python
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_max_depth(root: Node) -> int:
    if not root:
        return 0
    return pre_order_traversal(root, 0) # 0 is the starting height

def pre_order_traversal(node: Node, curr_depth: int):
    # The idea is that we want to traverse the left and the right subtree and compare which one has a deeper height
    if node.left:
        left_subtree_height = pre_order_traversal(node.left, curr_depth + 1)

    elif not node.left:
        left_subtree_height = curr_depth

    if node.right:
        right_subtree_height = pre_order_traversal(node.right, curr_depth + 1)

    elif not node.right:
        right_subtree_height = curr_depth

    max_subtree_height = max(left_subtree_height, right_subtree_height)

    return max_subtree_height


# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    root = build_tree(iter(input().split()), int)
    res = tree_max_depth(root)
    print(res)
```

### Approach 2

```python
def pre_order_traversal(node: Node, curr_depth: int):
    # The idea is that we want to traverse the left and the right subtree and compare which one has a deeper height
    if not node:you'
        return curr_depth - 1

    left_subtree_height = pre_order_traversal(node.left, curr_depth + 1)

    right_subtree_height = pre_order_traversal(node.right, curr_depth + 1)

    max_subtree_height = max(left_subtree_height, right_subtree_height)

    return max_subtree_height
```

Test cases:

1. normal binary tree
2. empty tree
3. tree with only one node
4. Linear tre
