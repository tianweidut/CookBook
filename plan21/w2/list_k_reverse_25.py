# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head
        
        left = right = head
        for i in range(0, k):
            if right is None:
                return head
            right = right.next
            
        new_head = self.reverse(left, right)
        head.next = self.reverseKGroup(right, k)
        return new_head
            
        
    def reverse(self, head, tail):
        prev = None
        
        while head != tail:
            successor = head.next
            head.next = prev
            prev = head
            head = successor
            
        return prev