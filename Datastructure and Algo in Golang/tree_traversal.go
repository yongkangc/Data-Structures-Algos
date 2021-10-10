package main

import "fmt"

// Binary Tree
type Node struct {
	val   int
	left  *Node
	right *Node
}

type BinaryTree struct {
	Root *Node
}

func createBinaryTree() *BinaryTree {
	root := &Node{
		val:   1,
		left:  &Node{val: 2},
		right: &Node{val: 3},
	}
	tree := &BinaryTree{root}
	tree.Root.left = &Node{val: 4}
	tree.Root.right = &Node{val: 5}
	return tree
}

func addRecursiveNode(node *Node, val int) *Node {
	if node == nil {
		return &Node{val: val}
	}

	if val < node.val {
		node.left = addRecursiveNode(node.left, val)
	} else {
		node.right = addRecursiveNode(node.right, val)
	}
	return node
}

func addNode(tree *BinaryTree, value int) {
	tree.Root = addRecursiveNode(tree.Root, value)
}

// Preorder Tree Traversal
func preOrderTraversal(node *Node) {
	if node == nil {
		return
	}
	// visit current node first
	fmt.Println(node)
	preOrderTraversal(node.left)
	preOrderTraversal(node.right)
}

// In order Tree Traversal
func inOrderTreeTraversal(node *Node) {
	if node == nil {
		return
	}
	inOrderTreeTraversal(node.left)
	fmt.Println(node)
	inOrderTreeTraversal(node.right)

}

func postOrderTraversal(node *Node) {
	if node == nil {
		return
	}
	preOrderTraversal(node.left)
	preOrderTraversal(node.right)
	fmt.Println(node)
}

func main() {
	// create binary tree
	tree := createBinaryTree()
	// add node to tree
	addNode(tree, 6)

	// Visualising the tree
	fmt.Println("Preorder Traversal:")
	preOrderTraversal(tree.Root)
	fmt.Println("\nInorder Traversal:")
	inOrderTreeTraversal(tree.Root)
	fmt.Println("\nPostorder Traversal:")
	postOrderTraversal(tree.Root)

}
