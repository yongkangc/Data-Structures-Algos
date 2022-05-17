# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# what we can do is a fast pointer which jumps 2, and the slow pointer which jumps 1

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while slow.next and fast:
            if fast == slow:
                return True
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                return False

        return False
