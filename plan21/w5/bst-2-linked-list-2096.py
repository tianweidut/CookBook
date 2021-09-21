"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        
        self.prev = None
        self.head = None
        
        self.traverse(root)
        self.head.left = self.prev
        self.prev.right = self.head
        
        return self.head
        
    def traverse(self, root):
        if not root:
            return None
        
        self.traverse(root.left)
        if self.prev:
            root.left = self.prev
            self.prev.right = root
            self.prev = root
        else:
            self.head = root
            self.prev = root
        self.traverse(root.right)
        