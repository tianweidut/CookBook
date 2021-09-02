# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        sentinel = ListNode(next=head)
        slow = sentinel
        high = head
        it = 0
        
        while high != None and high.next != None:
            high = high.next
            it += 1
            
            if it >= n:
                slow = slow.next
                
        slow.next = slow.next.next
        return sentinel.next
        