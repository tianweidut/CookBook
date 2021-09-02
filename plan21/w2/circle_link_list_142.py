# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        slow = fast = head
        
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            
            if slow == fast:
                slow = head
                
                while slow is not fast:
                    slow = slow.next
                    fast = fast.next
                    
                return slow
            
        return None