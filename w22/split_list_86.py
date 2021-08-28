# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition_val(self, head: ListNode, x: int) -> ListNode:
        smaller = ListNode()
        larger = ListNode()
        saved_larger = larger
        saved_smaller = smaller

        while head is not None:
            if head.val < x:
                smaller.next = ListNode(val=head.val)
                smaller = smaller.next
            else:
                larger.next = ListNode(val=head.val)
                larger = larger.next
            head = head.next

        smaller.next = saved_larger.next
        return saved_smaller.next

    def partition(self, head: ListNode, x: int) -> ListNode:
        smaller = ListNode()
        larger = ListNode()
        saved_larger = larger
        saved_smaller = smaller

        while head is not None:
            if head.val < x:
                smaller.next = head
                smaller = smaller.next
            else:
                larger.next = head
                larger = larger.next
            head = head.next

        larger.next = None
        smaller.next = saved_larger.next
        return saved_smaller.next