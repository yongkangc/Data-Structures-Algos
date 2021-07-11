package main

func twoSum(nums []int, target int) []int {

}

func main() {
	input_15, target_15 := [5]int{2, 3, 9, 5, 6}, 15
	if twoSum(input_15, target_15) != [2]int{2, 4} {
		panic("error for 15")
	}

}
