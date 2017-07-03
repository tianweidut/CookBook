
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        if n < 0:
            return head

        cnt = 1
        orig = phead = head
        while phead:
            phead = phead.next
            if cnt == n:
                break
            cnt += 1

        if cnt != n:
            return orig

        while phead and phead.next:
            head = head.next
            phead = phead.next

        if head == orig:
            return head.next
        else:
            head.next = head.next.next
            return orig
