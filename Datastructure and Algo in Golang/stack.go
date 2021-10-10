package main

// stack is a LIFO data structure
type stack struct {
	data []int
}

// NewStack creates a new stack
func NewStack() *stack {
	return &stack{data: make([]int, 0)}
}

// Push pushes an integer to the stack
func (s *stack) Push(v int) {
	s.data = append(s.data, v)
}

//Pop pops an integer from the stack
func (s *stack) Pop() int {
	if len(s.data) == 0 {
		return 0
	}
	last := len(s.data) - 1
	v := s.data[last]
	s.data = s.data[:last]
	return v
}

// Peek peek the top of the stack
func (s *stack) Peek() int {
	if len(s.data) == 0 {
		return 0
	}
	return s.data[len(s.data)-1]
}

// Len returns the length of the stack
func (s *stack) Len() int {
	return len(s.data)
}

// IsEmpty checks if the stack is empty
func (s *stack) IsEmpty() bool {
	return s.Len() == 0
}
