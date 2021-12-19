
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        fake_head = ListNode(None)
        fake_head.next = head

        while head and head.next:
            head = head.next
        orig_end = end = head

        if fake_head.next == end:
            return fake_head.next

        head = fake_head
        while head.next != orig_end:
            if head.next.val < x:
                head = head.next
            else:
                node = head.next
                end.next = node
                end = end.next
                head.next = node.next
                node.next = None

        if orig_end.val >= x and orig_end != end:
            head.next = orig_end.next
            orig_end.next = None
            end.next = orig_end

        return fake_head.next
