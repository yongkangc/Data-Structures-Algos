# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# https://leetcode.com/problems/merge-k-sorted-lists/

# HEAP SORT
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return 
        
        heap = []

        for node in lists:
            while node:
                heapq.heappush(heap,node.val)
                node = node.next
        
        # create sorted list
        if not heap:
            return
        
        rootNode = ListNode(heapq.heappop(heap))
        node1 = rootNode
        
        while heap:
            value = heapq.heappop(heap)
            next_node = ListNode(value)
            node1.next = next_node
            node1 = next_node
        
        return rootNode

        