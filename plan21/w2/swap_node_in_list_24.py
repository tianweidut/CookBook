# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if head is None or head.next is None:
            return head
        
        next = head.next
        successor = self.swapPairs(next.next)
        head.next.next = head
        head.next = successor
        return next