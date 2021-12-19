# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        curr = head
        next = head.next
        sentinel = ListNode(next=head)
        ancenstor = sentinel
        
        while curr is not None and next is not None:
            if curr.val != next.val:
                ancenstor = curr
                next = next.next
                curr = curr.next
            else:
                while next is not None and next.next is not None:
                    if curr.val == next.next.val:
                        next = next.next
                    else:
                        break
                        
                ancenstor.next = next.next
                curr = next.next
                next = curr.next if curr else None
                
        return sentinel.next
        