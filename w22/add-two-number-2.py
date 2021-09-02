# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sentinel = ListNode()
        head = sentinel

        add = 0
        while l1 is not None or l2 is not None:
            if l1:
                v1 = l1.val
                l1 = l1.next
            else:
                v1 = 0

            if l2:
                v2 = l2.val
                l2 = l2.next
            else:
                v2 = 0

            val = v1 + v2 + add
            add = val // 10
            head.next = ListNode(val = val % 10)
            head = head.next

        if add != 0:
            head.next = ListNode(val = add)
        
        return sentinel.next