# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head;
        
        curr = head;
        next = curr.next
        
        while curr is not None and next is not None: 
            if curr.val == next.val:
                curr.next = next.next
            else:
                curr = next
            
            next = next.next
        
        return head