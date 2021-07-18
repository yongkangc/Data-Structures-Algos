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

	nodeEnd := l.head
	for nodeEnd.next != nil {
		nodeEnd = nodeEnd.next
	}
	nodeEnd.next = node
	fmt.Println(nodeEnd.next.data)

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
	for node := l.head; node != nil; node = node.next {
		fmt.Printf("%v -> ", node.data)

	}

}

// main method
func main() {

	var linkedList LinkedList

	linkedList = LinkedList{}

	linkedList.AddToHead(1)
	linkedList.AddToHead(3)
	linkedList.AddToEnd(10)

	linkedList.Display()
}
