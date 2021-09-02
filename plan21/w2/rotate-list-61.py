# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        orig_head = head
        last = None
        n = 0
        while head is not None:
            last = head
            head = head.next
            n += 1
            
        last.next = orig_head
        
        head = orig_head
        end = n - k % n
        i = 1
        while i < end:
            i += 1
            head = head.next
            
        tmp = head
        head = head.next
        tmp.next = None
            
        return head
        