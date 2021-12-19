# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []
        
        def _r(n):
            if n is None:
                return
            
            _r(n.next)
            res.append(n.val)
            
        _r(head)
        
        return res