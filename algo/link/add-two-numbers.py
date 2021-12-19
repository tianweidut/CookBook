
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        degree = 0
        fake_head = ListNode(None)
        head = fake_head

        while l1 or l2:
            val = degree
            if l1:
                val += l1.val
                l1 = l1.next

            if l2:
                val += l2.val
                l2 = l2.next

            degree = val / 10
            val = val % 10
            head.next = ListNode(val)
            head = head.next

        if degree == 1:
            head.next = ListNode(degree)

        return fake_head.next
