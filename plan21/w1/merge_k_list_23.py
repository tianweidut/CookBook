# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ItListNode():
    def __init__(self, node):
        self.node = node
        
    def __lt__(self, other):
        return self.node.val < other.node.val 
        

class Solution:
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq
        
        sentinel = ListNode()
        head = sentinel
        
        heap = []
        
        for node in lists:
            if not node:
                continue
            heapq.heappush(heap, ItListNode(node))
            
            
        while len(heap) != 0:
            min_node = heapq.heappop(heap).node
            head.next = min_node
            head = head.next
            
            min_node = min_node.next
            if min_node:
                heapq.heappush(heap, ItListNode(min_node))
        
        return sentinel.next