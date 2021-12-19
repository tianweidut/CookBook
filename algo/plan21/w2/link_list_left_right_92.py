# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        self.successor = None
        return self._do_reverse(head, left, right)
        
    def _do_reverse(self, head, left, right):
        if left > 1:
            head.next = self._do_reverse(head.next, left-1, right-1)
            return head
        elif left <= 1:
            if right == 1:
                self.successor = head.next
                return head
            else:
                last = self._do_reverse(head.next, left, right-1)
                head.next.next = head
                head.next = self.successor
                return last
            
            
        