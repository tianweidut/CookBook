
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head

        fake_head = ListNode(None)
        fake_head.next = head
        prev = fake_head

        while head:
            if head.val == val:
                prev.next = head.next
                head = head.next
            else:
                prev = head
                head = head.next

        return fake_head.next
