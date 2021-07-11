// linked list implementation
package main

import "fmt"

// operations of linked list

// append
// remove node
// traverse

// node
type Node struct {
	prev *Node
	next *Node
	data interface{}
}

// Linked List
type LinkedList struct {
	head *Node
	tail *Node
}

// Linked List Insert to the end
func (l *LinkedList) PushBack(data interface{}) {
	// Get memory of Linked List
	list := &Node{
		next: l.head,
		data: data,
	}

	// add next node to tail, and previous
	// change linked list tail to current one

}

// Note on Pointer
// Pointers reference a location in memory where a value is stored rather than the value itself.
//  (They point to something else)
// By using a pointer (*int) the zero function is able to modify the original variable.

// `&` goes in front of a variable when you want to get that variable's memory address.
