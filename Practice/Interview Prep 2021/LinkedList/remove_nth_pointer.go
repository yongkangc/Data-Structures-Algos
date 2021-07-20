/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 func removeNthFromEnd(head *ListNode, n int) *ListNode {
    preHeader := &ListNode{Next: head}
    
    left, right := preHeader, head
  for i := 0; right != nil && i < n; i++ {
        right = right.Next
    }
    for right != nil {
        left, right = left.Next, right.Next
    }
    left.Next = left.Next.Next
    return preHeader.Next
}   

// find the length of the linkedlist by traversing through
// double pointer method where it is split by n
// once the right pointer reach the end, remove the node
// Time complexity : O(n) , Space Complexity : O(1
// We employ a node called the preHeader node, whose Next pointer points to the head of our list.
// Then we point our left pointer to the preHeader to start off with. (Figure 4)
// The advantage of this approach is that, when our right pointer gets to the end of our list, left will be pointing to the node just before the Nth node from the end, which makes deleting that node very straight forward. 