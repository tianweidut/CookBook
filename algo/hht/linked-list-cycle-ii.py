
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
    @return: The node where the cycle begins.
                if there is no cycle, return null
    """

    def detectCycle(self, head):
        if not head:
            return None

        slow = head
        fast = head
        while True:
            if slow and fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            else:
                return None

            if slow == fast:
                break

        if not slow or not fast:
            return None

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
