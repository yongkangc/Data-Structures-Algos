package main

import "fmt"

type Node struct {
	next *Node
	prev *Node
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
		prev: nil,
		data: data,
	}

	nodeEnd := l.head
	for nodeEnd.next != nil {
		nodeEnd = nodeEnd.next
	}
	nodeEnd.next = node
	node.prev = nodeEnd

	l.length++
}

func (l *LinkedList) AddToHead(data interface{}) {
	// creating a node with the data
	var node = &Node{
		next: nil,
		prev: nil,
		data: data,
	}

	if l.head != nil {
		l.head.prev = node
		node.next = l.head
	}

	l.head = node
	l.length++

}

func (l *LinkedList) Len() int {
	return l.length
}

func (l *LinkedList) DisplayForward() {
	var node *Node
	for node = l.head; node != nil; node = node.next {
		fmt.Printf("%v -> ", node.data)

	}
}

func (l *LinkedList) DisplayBackwards() {
	var node *Node
	for node = l.tail; node != nil; node = node.prev {
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

	// linkedList.DisplayForward()
	// fmt.Println("-----")
	linkedList.DisplayBackwards()

}
