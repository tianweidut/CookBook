
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        fake_head = ListNode(None)
        head = fake_head
        
        import heapq
        hq = [(node.val, node) for node in lists if node]
        heapq.heapify(hq)
        
        while hq:
            top = heapq.heappop(hq)
            head.next = ListNode(top[0])
            head = head.next
            
            if top[1].next:
                heapq.heappush(hq, (top[1].next.val, top[1].next))
        
        return fake_head.next
