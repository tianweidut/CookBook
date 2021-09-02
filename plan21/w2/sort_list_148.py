# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        left = head
        right = self.split(head)
        
        s_left = self.sortList(left)
        s_right = self.sortList(right)
        
        return self.merge(s_left, s_right)
        
    
    def split(self, head):
        if head is None or head.next is None:
            return head
        
        slow = ListNode(next=head)
        fast = head
        
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        
        target = slow.next
        slow.next = None
        
        return target
    
    def merge(self, l1, l2):
        sentinel = ListNode()
        head = sentinel
        
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
        
        if l1: head.next = l1
        if l2: head.next = l2
            
        return sentinel.next
    
    