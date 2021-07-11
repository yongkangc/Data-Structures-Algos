package main

import "fmt"

func main() {
	x := 4
	fmt.Println(&x)
	square(x)

	// when you call the fucntion with pointer, you need to pass in the adddress
	squarePointer(&x)
}

func square(x int) {
	x *= x
	fmt.Println(&x, x)
}

// this function modifies the value through pointer
func squarePointer(x *int) {
	// putting star to access value at x. x is the address
	*x *= *x
	fmt.Println(x, *x)
}
