package main

import "fmt"

type Node struct {
	next *Node
	data interface{}
}

type LinkedList struct {
	head   *Node
	tail   *Node
	length int
}

func (l *LinkedList) AddToEnd(data interface{}) {
	// creating a node with the data
	var node = &Node{
		next: nil,
		data: data,
	}

	if l.tail == nil {
		l.tail = node
	} else {
		l.tail.next = node
		l.tail = node
	}
	l.length++
}

func (l *LinkedList) AddToHead(data interface{}) {
	// creating a node with the data
	var node = &Node{
		next: nil,
		data: data,
	}

	if l.head != nil {
		node.next = l.head
	}

	l.head = node
	l.length++

}

func (l *LinkedList) Len() int {
	return l.length
}

func (l *LinkedList) Display() {
	var node *Node
	for node = l.head; node != nil; node = node.next {
		fmt.Printf("%v -> ", node.data)

	}

}

// main method
func main() {

	var linkedList LinkedList

	linkedList = LinkedList{}

	linkedList.AddToHead(1)
	linkedList.AddToHead(3)
	linkedList.AddToEnd(5)

	linkedList.Display()

}
