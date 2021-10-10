package main

// build heap
func main() {
	var heap [5]int
	heap[0] = 5
	heap[1] = 4
	heap[2] = 3
	heap[3] = 2
	heap[4] = 1
	heapify(heap, 5)
	for i := 0; i < 5; i++ {
		fmt.Println(heap[i])
	}
}