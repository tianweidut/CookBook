
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        node = self.partition(head)
        l1 = self.sortList(head)
        l2 = self.sortList(node)

        return self.merge(l1, l2)

    def partition(self, node):
        if not node or not node.next:
            return node

        fake_head = ListNode(None)
        fake_head.next = node
        pl = fake_head
        nl = node

        while nl and nl.next:
            pl = pl.next
            nl = nl.next.next

        p_node = pl.next
        pl.next = None
        return p_node

    def merge(self, l1, l2):
        fake_head = ListNode(None)
        head = fake_head

        while l1 and l2:
            if l1.val < l2.val:
                head.next = ListNode(l1.val)
                l1 = l1.next
            else:
                head.next = ListNode(l2.val)
                l2 = l2.next
            head = head.next

        if l1:
            head.next = l1

        if l2:
            head.next = l2

        return fake_head.next
