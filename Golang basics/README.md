# Basics for Golang

## Table of contents

1. [Pointers](#Pointers)

### Pointers

Why use pointer?

- efficent to store variables in one place and access it in one place rather than cloning it
- changing variable in function (ensuring immutability)

pointer points to a address in memory.

Accessing memory address : `&variable`

```golang
i, j := 42, 120
fmt.Println(&i, &j)

>> 0xc000014098 0xc0000140b0
```

pointer type : `*datatype` e.g int

pointer variable : `*variable` i.e value at that address

```golang
	i, j := 42, 120
	p := &i
	fmt.Println(p)
	fmt.Println(*p)
>> 42
>> 0xc000014098
```

Example of Using pointers in functions

```golang
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
>> 0xc0000ac058
>> 0xc0000ac090 16
>> 0xc0000ac058 16
```

![alt text](../assets/pointers1.PNG "functions and pointers")

Heaps
