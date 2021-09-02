# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return

        sentinel = ListNode(next=head)
        slow = sentinel
        fast = head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        right = self.reverse(slow.next)
        slow.next = None
        left = sentinel.next

        curr = left
        next = right

        while curr is not None and next is not None:
            next_next = curr.next
            curr.next = next
            curr = next
            next = next_next

    def reverse(self, head):
        prev = None
        while head is not None:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        return prev