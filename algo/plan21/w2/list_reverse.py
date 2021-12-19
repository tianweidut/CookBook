# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        prev = None
        while head is not None:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
            
        return prev