# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        self.left = head
        
        return self.traverse(self.left)
        
    def traverse(self, right):
        if right is None:
            return True
        
        res = self.traverse(right.next)
        res = res and (self.left.val == right.val)
        self.left = self.left.next
        return res