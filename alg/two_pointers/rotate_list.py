
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k <= 0:
            return head

        len_link = 0
        phead = head
        while phead:
            len_link += 1
            phead = phead.next

        k = k % len_link
        if k == 0:
            return head

        fake_head = ListNode(None)
        fake_head.next = head

        prev = head = fake_head

        cnt = 0
        while cnt < k and head:
            head = head.next
            cnt += 1

        while head and head.next:
            head = head.next
            prev = prev.next

        if head and prev != fake_head:
            orig = fake_head.next
            fake_head.next = prev.next
            prev.next = None
            head.next = orig

        return fake_head.next
