
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fake_head = ListNode(None)
        fake_head.next = head
        prev = head = fake_head

        cnt = 0
        while cnt < n and head:
            head = head.next
            cnt += 1

        while head and head.next:
            head = head.next
            prev = prev.next

        if prev.next:
            prev.next = prev.next.next
        else:
            prev.next = None

        return fake_head.next
