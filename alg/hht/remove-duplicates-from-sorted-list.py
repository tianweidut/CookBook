

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
        fake_head = ListNode(None, next=head)
        prev = fake_head

        while head:
            while head.next and head.val == head.next.val:
                head = head.next

            prev.next = head
            prev = head
            head = head.next

        return fake_head.next
