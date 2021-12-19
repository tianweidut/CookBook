
# Definition for singly-linked list with a random pointer.


class RandomListNode:

    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode

    def copyRandomList(self, head):
        if not head:
            return None

        copy_map = {}

        orig_head = head
        rhead = chead = RandomListNode(head.label)

        while head:
            copy_map[head] = chead
            chead.next = RandomListNode(head.next.label) if head.next else None

            head = head.next
            chead = chead.next

        head = orig_head
        while head:
            c_node = copy_map[head]
            c_node.random = copy_map[head.random] if head.random else None
            head = head.next

        return rhead
