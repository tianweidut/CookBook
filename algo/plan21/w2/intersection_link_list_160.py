# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        an = 0
        la = headA
        while headA is not None:
            headA = headA.next
            an += 1
            
        bn = 0
        lb = headB
        while headB is not None:
            headB = headB.next
            bn += 1
        
        while la is not None and lb is not None:
            if an > bn:
                la = la.next
                an -= 1
            elif an < bn:
                lb = lb.next
                bn -= 1
            else:
                if la is lb:
                    return la
                
                la = la.next
                lb = lb.next
                an -= 1
                bn -= 1
        
        return None
            