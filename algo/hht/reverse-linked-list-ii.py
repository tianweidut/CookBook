"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: The head of linked list
    @param m: start position
    @param n: end position
    """
    def reverseBetween(self, head, m, n):
        if not head or m >= n or m <= 0 or n <= 0:
            return head

        #也可能m(n) > head的最大长度
        rhead = head
        pprev = None
        nnext = None

        prev = None
        cnt = 1

        while head and cnt <= n:
            if cnt < m:
                pprev = head
                head = head.next
            elif cnt == m:
                prev = head
                head = head.next
            elif cnt > m:
                nnext = head.next
                head.next = prev
                prev = head
                head = nnext

            cnt += 1

        if pprev:
            t = pprev.next
            pprev.next = prev
            t.next = nnext

        return prev if m != 1 else rhead
