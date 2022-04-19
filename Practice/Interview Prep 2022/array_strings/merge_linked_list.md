My Approach
```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # approach is two have two pointers in the list, and compare. 
        # clone the list node onto the head of 
        new_list = ListNode(-1)
        current = new_list
        
        while list1 != None or list2 != None:
            # check if any one list if None. if none we can append it to the end of list
            if list1 == None:
                while list2 != None:
                    current.next = ListNode(list2.val)
                    current = current.next
                    list2 = list2.next
            
            elif list2 == None: # append l1 to end of new_list
                while list1 != None:
                    current.next = ListNode(list1.val)
                    current = current.next
                    list1 = list1.next
                    
            # compare l1 and l2 node
            else:
                if list1.val > list2.val:
                    current.next = ListNode(list2.val)
                    current = current.next
                    list2 = list2.next
                    
                else:
                    current.next = ListNode(list1.val)
                    current = current.next
                    list1 = list1.next
        
        return new_list.next
```