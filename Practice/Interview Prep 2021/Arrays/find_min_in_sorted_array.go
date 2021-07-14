func findMin(nums []int) int {    
    // base case

    if len(nums) == 1{
        return nums[0]
    }
    
    if len(nums) == 2{
        return min(nums[0],nums[1])
    } else{
        // find the middle
        mid := len(nums) /2
        
        // if right is less than mid, return right
        if nums[mid+1]<nums[mid]{
            return nums[mid+1]
        }
        // if left is more, return that number
        if nums[mid-1] > nums[mid]{
            return nums[mid]
        }else{
            // if left is less, continue bisection with left and right array to find smallest
            return min(findMin(nums[:mid]),findMin(nums[mid+1:]))
                       }
                       
    
    
}
}


func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

// Time Complexity : Same as Binary Search O(\log N)O(logN)
// Space Complexity : O(1)O(1)