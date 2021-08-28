# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList1(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        odd = head
        even = head.next
        saved_even = even

        while odd.next is not None and even.next is not None:
            odd.next = even.next
            odd = odd.next
            
            if odd.next:
                even.next = odd.next
                even = even.next

        even.next = None
        odd.next = saved_even
        return head

    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        odd, even = head, head.next
        saved_even = even

        while even is not None and even.next is not None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = saved_even
        return head
        