

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Solution:

    """
    @param two ListNodes
    @return a ListNode
    """

    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2

        if not l2:
            return l1

        phead = None
        head = None

        while l1 and l2:
            if l1.val <= l2.val:
                cur = l1.val
                l1 = l1.next
            else:
                cur = l2.val
                l2 = l2.next

            if head is None:
                head = ListNode(cur)
                phead = head
            else:
                head.next = ListNode(cur)
                head = head.next

        while l1:
            head.next = ListNode(l1.val)
            head = head.next
            l1 = l1.next

        while l2:
            head.next = ListNode(l2.val)
            head = head.next
            l2 = l2.next

        return phead
