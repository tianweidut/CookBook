

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:

    """
    @param head: A ListNode
    @return: A ListNode
    """

    def deleteDuplicates(self, head):
        if not head:
            return None

        ohead = head
        next = head.next

        while head:
            if next is None:
                head.next = next
                head = next
            else:
                if head.val == next.val:
                    next = next.next
                else:
                    head.next = next
                    head = next

        return ohead
