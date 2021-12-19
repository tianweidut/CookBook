
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:

    """
    @param head: The first node of the linked list.
    @return: True if it has a cycle, or false
    """

    def hasCycle_with_map(self, head):
        if not head:
            return False

        node_map = set()

        while head:
            if head in node_map:
                return True
            node_map.add(head)
            head = head.next

        return False

    def hasCycle(self, head):
        if not head:
            return False

        next_two = head.next

        while head and next_two:
            if head == next_two:
                return True

            head = head.next
            if next_two.next:
                next_two = next_two.next.next
            else:
                return False

        return False
