# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        sentinel = ListNode()
        head = sentinel
        
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
                
            head = head.next
                
        if l1: head.next = l1
        if l2: head.next = l2
        
        return sentinel.next