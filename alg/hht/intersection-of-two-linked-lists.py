

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param headA: the first list
    # @param headB: the second list
    # @return: a ListNode
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None

        orig_headA = headA
        orig_headB = headB

        len_a = self.get_list_len(headA)
        len_b = self.get_list_len(headB)

        common_cnt = len_a

        if len_a > len_b:
            common_cnt = len_b
            diff = len_a - len_b
            while diff:
                headA = headA.next
                diff -= 1

        if len_b > len_a:
            common_cnt = len_a
            diff = len_b - len_a
            while diff:
                headB = headB.next
                diff -= 1

        find_node = None
        while common_cnt:
            if headA == headB:
                find_node = headA
                break

            headA = headA.next
            headB = headB.next

        headA = orig_headA
        headB = orig_headB
        return find_node

    def get_list_len(self, head):
        cnt = 0

        c_head = head
        while c_head:
            c_head = c_head.next
            cnt += 1

        return cnt
